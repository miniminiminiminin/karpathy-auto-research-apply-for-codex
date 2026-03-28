from __future__ import annotations

import argparse
import json
import re
from datetime import datetime
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo-root", default="")
    parser.add_argument("--type", required=True, choices=("failure", "difficulty", "error"))
    parser.add_argument("--summary", required=True)
    parser.add_argument("--context", default="")
    parser.add_argument("--problem", default="")
    parser.add_argument("--cause", default="")
    parser.add_argument("--fix", default="")
    parser.add_argument("--lesson", required=True)
    parser.add_argument("--reusable", choices=("yes", "no"), required=True)
    parser.add_argument("--promotion-target", choices=("skill", "asset", "reference", "rule", "none"), default="none")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    repo_root = resolve_repo_root(args.repo_root)
    lessons_root = repo_root / ".codex" / "lessons"
    record_path = write_record(args, lessons_root / "records")
    append_index(args, repo_root, lessons_root, record_path)
    print(
        json.dumps(
            {
                "record": str(record_path.relative_to(repo_root)),
                "type": args.type,
                "summary": args.summary,
                "promotion_target": args.promotion_target,
            },
            ensure_ascii=False,
        )
    )
    return 0


def resolve_repo_root(override: str) -> Path:
    if override:
        return Path(override).expanduser().resolve()
    return Path(__file__).resolve().parents[4]


def write_record(args: argparse.Namespace, records_dir: Path) -> Path:
    stamp = datetime.now().astimezone().strftime("%Y-%m-%d")
    slug = slugify(args.summary)
    records_dir.mkdir(parents=True, exist_ok=True)
    path = next_record_path(records_dir, stamp, slug)
    path.write_text(
        "\n".join(
            [
                "# Lesson Record",
                "",
                f"- type: {args.type}",
                f"- summary: {args.summary}",
                f"- context: {args.context}",
                f"- observed problem: {args.problem}",
                f"- root cause or hypothesis: {args.cause}",
                f"- workaround or fix: {args.fix}",
                f"- reusable lesson: {args.lesson}",
                f"- reusable: {args.reusable}",
                f"- promotion target: {args.promotion_target}",
                "- promotion status: pending",
                "- target path: ",
                "",
            ]
        ),
        encoding="utf-8",
    )
    return path


def next_record_path(records_dir: Path, stamp: str, slug: str) -> Path:
    base_name = f"{stamp}-{slug}"
    candidate = records_dir / f"{base_name}.md"
    if not candidate.exists():
        return candidate
    counter = 2
    while True:
        candidate = records_dir / f"{base_name}-{counter}.md"
        if not candidate.exists():
            return candidate
        counter += 1


def append_index(args: argparse.Namespace, repo_root: Path, lessons_root: Path, record_path: Path) -> None:
    lessons_root.mkdir(parents=True, exist_ok=True)
    index_path = lessons_root / "index.jsonl"
    with index_path.open("a", encoding="utf-8") as handle:
        handle.write(
            json.dumps(
                {
                    "timestamp": datetime.now().astimezone().isoformat(),
                    "type": args.type,
                    "summary": args.summary,
                    "record": str(record_path.relative_to(repo_root)),
                    "reusable": args.reusable == "yes",
                    "promotion_target": args.promotion_target,
                    "promotion_status": "pending",
                },
                ensure_ascii=False,
            )
            + "\n"
        )


def slugify(value: str) -> str:
    cleaned = re.sub(r"[^a-zA-Z0-9가-힣]+", "-", value.strip()).strip("-").lower()
    return cleaned or "lesson"


if __name__ == "__main__":
    raise SystemExit(main())
