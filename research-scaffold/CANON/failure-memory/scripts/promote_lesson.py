from __future__ import annotations

import argparse
import json
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo-root", default="")
    parser.add_argument("--record", required=True)
    parser.add_argument("--status", required=True, choices=("pending", "promoted", "dismissed"))
    parser.add_argument("--target-path", default="")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    repo_root = resolve_repo_root(args.repo_root)
    record_path = resolve_record_path(repo_root, args.record)
    ensure_repo_local_record(repo_root, record_path)
    update_record(record_path, args.status, args.target_path)
    update_index(repo_root, record_path, args.status, args.target_path)
    print(
        json.dumps(
            {
                "record": str(record_path.relative_to(repo_root)),
                "status": args.status,
                "target_path": args.target_path,
            },
            ensure_ascii=False,
        )
    )
    return 0


def resolve_repo_root(override: str) -> Path:
    if override:
        return Path(override).expanduser().resolve()
    return Path(__file__).resolve().parents[4]


def resolve_record_path(repo_root: Path, record: str) -> Path:
    record_path = Path(record)
    if not record_path.is_absolute():
        record_path = (repo_root / record_path).resolve()
    return record_path


def ensure_repo_local_record(repo_root: Path, record_path: Path) -> None:
    allowed_root = (repo_root / ".codex" / "lessons" / "records").resolve()
    if not record_path.exists():
        raise SystemExit(f"record does not exist: {record_path}")
    try:
        record_path.relative_to(allowed_root)
    except ValueError as error:
        raise SystemExit(f"record must live under {allowed_root}") from error


def update_record(record_path: Path, status: str, target_path: str) -> None:
    lines = record_path.read_text(encoding="utf-8").splitlines()
    updated: list[str] = []
    saw_status = False
    saw_target = False
    for line in lines:
        if line.startswith("- promotion status:"):
            updated.append(f"- promotion status: {status}")
            saw_status = True
        elif line.startswith("- target path:"):
            updated.append(f"- target path: {target_path}")
            saw_target = True
        else:
            updated.append(line)
    if not saw_status:
        updated.append(f"- promotion status: {status}")
    if not saw_target:
        updated.append(f"- target path: {target_path}")
    record_path.write_text("\n".join(updated) + "\n", encoding="utf-8")


def update_index(repo_root: Path, record_path: Path, status: str, target_path: str) -> None:
    index_path = repo_root / ".codex" / "lessons" / "index.jsonl"
    if not index_path.exists():
        return
    record_key = str(record_path.relative_to(repo_root))
    rows = []
    for raw in index_path.read_text(encoding="utf-8").splitlines():
        if not raw.strip():
            continue
        payload = json.loads(raw)
        if payload.get("record") == record_key:
            payload["promotion_status"] = status
            payload["target_path"] = target_path
        rows.append(payload)
    index_path.write_text(
        "".join(json.dumps(row, ensure_ascii=False) + "\n" for row in rows),
        encoding="utf-8",
    )


if __name__ == "__main__":
    raise SystemExit(main())
