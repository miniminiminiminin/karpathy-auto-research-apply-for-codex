#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat <<'EOF'
Usage: verify-fix.sh

Reruns the bounded checks for a fixed target and writes a verification summary.

Required environment:
  NETWORK_NAME   Docker network containing the target
  TARGET_URL     Target URL on the lab network
  BASELINE_DIR   Previous run directory to compare against

Optional environment:
  RUN_ID         Verification run id
  OUTPUT_ROOT    Artifact root. Default: <repo>/artifacts/security-lab
  EXPECT_CLEAN   Set to 1 to fail when high or critical findings remain in nuclei output
EOF
}

if [[ "${1:-}" == "--help" ]]; then
  usage
  exit 0
fi

: "${NETWORK_NAME:?set NETWORK_NAME}"
: "${TARGET_URL:?set TARGET_URL}"
: "${BASELINE_DIR:?set BASELINE_DIR}"

script_dir="$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)"
skill_dir="$(CDPATH= cd -- "$script_dir/.." && pwd)"
repo_root="$(CDPATH= cd -- "$skill_dir/../../.." && pwd)"
OUTPUT_ROOT="${OUTPUT_ROOT:-$repo_root/artifacts/security-lab}"
verify_run_id="${RUN_ID:-verify-$(date +%Y%m%d-%H%M%S)}"

if ! command -v docker >/dev/null 2>&1; then
  echo "missing required command: docker" >&2
  exit 2
fi

RUN_ID="$verify_run_id" OUTPUT_ROOT="$OUTPUT_ROOT" NETWORK_NAME="$NETWORK_NAME" TARGET_URL="$TARGET_URL" \
  "$script_dir/run-web-checks.sh" >/dev/null

verify_dir="$OUTPUT_ROOT/$verify_run_id"
baseline_nuclei="$BASELINE_DIR/checks/nuclei.jsonl"
verify_nuclei="$verify_dir/checks/nuclei.jsonl"

count_lines() {
  if [[ -f "$1" ]]; then
    wc -l <"$1" | tr -d ' '
  else
    echo 0
  fi
}

baseline_count="$(count_lines "$baseline_nuclei")"
verify_count="$(count_lines "$verify_nuclei")"

cat >"$verify_dir/verification-summary.md" <<EOF
# Verification Summary

- baseline dir: $BASELINE_DIR
- verification dir: $verify_dir
- baseline nuclei findings: $baseline_count
- verification nuclei findings: $verify_count
EOF

if [[ "${EXPECT_CLEAN:-0}" == "1" ]] && [[ "$verify_count" != "0" ]]; then
  echo "verification failed: findings remain in $verify_nuclei" >&2
  exit 4
fi

printf 'verification complete\nverification_dir=%s\nsummary=%s\n' \
  "$verify_dir" "$verify_dir/verification-summary.md"
