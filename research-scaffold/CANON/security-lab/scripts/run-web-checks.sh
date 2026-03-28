#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat <<'EOF'
Usage: run-web-checks.sh

Runs bounded passive and active checks from disposable Docker tool containers.

Required environment:
  NETWORK_NAME  Docker network containing the target
  TARGET_URL    Target URL on the lab network

Optional environment:
  RUN_ID             Reuse an existing run directory name
  OUTPUT_ROOT        Artifact root. Default: <repo>/artifacts/security-lab
  ZAP_IMAGE          Default: ghcr.io/zaproxy/zaproxy:stable
  NUCLEI_IMAGE       Default: projectdiscovery/nuclei:latest
  SQLMAP_IMAGE       Default: ghcr.io/sqlmapproject/sqlmap:latest
  ENABLE_ACTIVE_SCAN Set to 1 to run ZAP full scan
  ENABLE_SQLMAP      Set to 1 to run sqlmap against SQLMAP_TARGET
  SQLMAP_TARGET      Exact URL with injectable parameter for sqlmap
  SQLMAP_DATA        Optional POST data for sqlmap
EOF
}

if [[ "${1:-}" == "--help" ]]; then
  usage
  exit 0
fi

: "${NETWORK_NAME:?set NETWORK_NAME}"
: "${TARGET_URL:?set TARGET_URL}"

script_dir="$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)"
skill_dir="$(CDPATH= cd -- "$script_dir/.." && pwd)"
repo_root="$(CDPATH= cd -- "$skill_dir/../../.." && pwd)"
OUTPUT_ROOT="${OUTPUT_ROOT:-$repo_root/artifacts/security-lab}"
ZAP_IMAGE="${ZAP_IMAGE:-ghcr.io/zaproxy/zaproxy:stable}"
NUCLEI_IMAGE="${NUCLEI_IMAGE:-projectdiscovery/nuclei:latest}"
SQLMAP_IMAGE="${SQLMAP_IMAGE:-ghcr.io/sqlmapproject/sqlmap:latest}"
run_id="${RUN_ID:-$(date +%Y%m%d-%H%M%S)}"
run_dir="$OUTPUT_ROOT/$run_id"
mkdir -p "$run_dir/checks"

if ! command -v docker >/dev/null 2>&1; then
  echo "missing required command: docker" >&2
  exit 2
fi

docker network inspect "$NETWORK_NAME" >/dev/null

target_host="${TARGET_URL#http://}"
target_host="${target_host#https://}"
target_host="${target_host%%/*}"
case "$target_host" in
  localhost*|127.*|0.0.0.0*|*.*)
    echo "TARGET_URL host must be a Docker lab alias, not localhost or public DNS: $target_host" >&2
    exit 2
    ;;
esac

docker run --rm --network "$NETWORK_NAME" -v "$run_dir/checks:/zap/wrk" "$ZAP_IMAGE" \
  zap-baseline.py -t "$TARGET_URL" -m 2 -J zap-baseline.json -w zap-baseline.md -r zap-baseline.html -x zap-baseline.xml \
  >"$run_dir/checks/zap-baseline.log" 2>&1 || true

if [[ "${ENABLE_ACTIVE_SCAN:-0}" == "1" ]]; then
  docker run --rm --network "$NETWORK_NAME" -v "$run_dir/checks:/zap/wrk" "$ZAP_IMAGE" \
    zap-full-scan.py -t "$TARGET_URL" -J zap-active.json -w zap-active.md -r zap-active.html -x zap-active.xml \
    >"$run_dir/checks/zap-active.log" 2>&1 || true
fi

docker run --rm --network "$NETWORK_NAME" -v "$run_dir/checks:/work" "$NUCLEI_IMAGE" \
  -u "$TARGET_URL" -severity low,medium,high,critical -json-export /work/nuclei.jsonl \
  >"$run_dir/checks/nuclei.log" 2>&1 || true

if [[ "${ENABLE_SQLMAP:-0}" == "1" ]]; then
  : "${SQLMAP_TARGET:?set SQLMAP_TARGET when ENABLE_SQLMAP=1}"
  sqlmap_args=(-u "$SQLMAP_TARGET" --batch --output-dir=/work/sqlmap)
  if [[ -n "${SQLMAP_DATA:-}" ]]; then
    sqlmap_args+=(--data "$SQLMAP_DATA")
  fi
  docker run --rm --network "$NETWORK_NAME" -v "$run_dir/checks:/work" "$SQLMAP_IMAGE" "${sqlmap_args[@]}" \
    >"$run_dir/checks/sqlmap.log" 2>&1 || true
fi

cat >"$run_dir/checks/summary.md" <<EOF
# Security Lab Check Summary

- target: $TARGET_URL
- network: $NETWORK_NAME
- zap baseline: $run_dir/checks/zap-baseline.log
- nuclei: $run_dir/checks/nuclei.log
- zap active enabled: ${ENABLE_ACTIVE_SCAN:-0}
- sqlmap enabled: ${ENABLE_SQLMAP:-0}
EOF

printf 'checks complete\nrun_dir=%s\nsummary=%s\n' \
  "$run_dir" "$run_dir/checks/summary.md"
