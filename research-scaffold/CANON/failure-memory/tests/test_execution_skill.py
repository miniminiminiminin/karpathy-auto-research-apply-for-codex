from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


SKILL_DIR = Path(__file__).resolve().parents[1]


def test_failure_memory_skill_runs_from_its_own_scripts(tmp_path: Path) -> None:
    repo_root = tmp_path / "repo"
    skill_root = repo_root / ".codex" / "skills" / "failure-memory"
    lessons_root = repo_root / ".codex" / "lessons"
    records_dir = lessons_root / "records"
    index_path = lessons_root / "index.jsonl"

    records_dir.mkdir(parents=True)
    index_path.write_text("", encoding="utf-8")

    copy_tree(SKILL_DIR, skill_root)

    log_script = skill_root / "scripts" / "log_lesson.py"
    promote_script = skill_root / "scripts" / "promote_lesson.py"

    log_result = subprocess.run(
        [
            sys.executable,
            str(log_script),
            "--repo-root",
            str(repo_root),
            "--type",
            "error",
            "--summary",
            "skill-local logging works",
            "--lesson",
            "keep execution scripts inside the skill package",
            "--reusable",
            "yes",
            "--promotion-target",
            "skill",
        ],
        check=True,
        capture_output=True,
        text=True,
    )

    payload = json.loads(log_result.stdout)
    record_path = repo_root / payload["record"]
    assert record_path.exists()
    assert "promotion status: pending" in record_path.read_text(encoding="utf-8")
    index_rows = [json.loads(line) for line in index_path.read_text(encoding="utf-8").splitlines() if line]
    assert index_rows[0]["promotion_status"] == "pending"

    subprocess.run(
        [
            sys.executable,
            str(promote_script),
            "--repo-root",
            str(repo_root),
            "--record",
            payload["record"],
            "--status",
            "promoted",
            "--target-path",
            ".codex/skills/failure-memory/SKILL.md",
        ],
        check=True,
        capture_output=True,
        text=True,
    )

    assert "promotion status: promoted" in record_path.read_text(encoding="utf-8")
    promoted_rows = [json.loads(line) for line in index_path.read_text(encoding="utf-8").splitlines() if line]
    assert promoted_rows[0]["promotion_status"] == "promoted"
    assert promoted_rows[0]["target_path"] == ".codex/skills/failure-memory/SKILL.md"


def test_log_lesson_keeps_distinct_records_for_same_summary(tmp_path: Path) -> None:
    repo_root = tmp_path / "repo"
    skill_root = repo_root / ".codex" / "skills" / "failure-memory"
    lessons_root = repo_root / ".codex" / "lessons"
    records_dir = lessons_root / "records"
    index_path = lessons_root / "index.jsonl"

    records_dir.mkdir(parents=True)
    index_path.write_text("", encoding="utf-8")
    copy_tree(SKILL_DIR, skill_root)

    log_script = skill_root / "scripts" / "log_lesson.py"
    payloads = []
    for _ in range(2):
        result = subprocess.run(
            [
                sys.executable,
                str(log_script),
                "--repo-root",
                str(repo_root),
                "--type",
                "error",
                "--summary",
                "same summary",
                "--lesson",
                "keep duplicate incidents as separate records",
                "--reusable",
                "yes",
                "--promotion-target",
                "skill",
            ],
            check=True,
            capture_output=True,
            text=True,
        )
        payloads.append(json.loads(result.stdout))

    assert payloads[0]["record"] != payloads[1]["record"]
    assert (repo_root / payloads[0]["record"]).exists()
    assert (repo_root / payloads[1]["record"]).exists()
    rows = [json.loads(line) for line in index_path.read_text(encoding="utf-8").splitlines() if line]
    assert len(rows) == 2


def test_promote_lesson_rejects_records_outside_lessons_store(tmp_path: Path) -> None:
    repo_root = tmp_path / "repo"
    skill_root = repo_root / ".codex" / "skills" / "failure-memory"
    lessons_root = repo_root / ".codex" / "lessons"
    records_dir = lessons_root / "records"
    index_path = lessons_root / "index.jsonl"
    outside_record = repo_root / "outside.md"

    records_dir.mkdir(parents=True)
    index_path.write_text("", encoding="utf-8")
    outside_record.write_text("# outside\n", encoding="utf-8")
    copy_tree(SKILL_DIR, skill_root)

    promote_script = skill_root / "scripts" / "promote_lesson.py"
    result = subprocess.run(
        [
            sys.executable,
            str(promote_script),
            "--repo-root",
            str(repo_root),
            "--record",
            str(outside_record),
            "--status",
            "promoted",
            "--target-path",
            ".codex/skills/failure-memory/SKILL.md",
        ],
        capture_output=True,
        text=True,
    )

    assert result.returncode != 0
    assert outside_record.read_text(encoding="utf-8") == "# outside\n"


def test_log_lesson_infers_repo_root_from_skill_path(tmp_path: Path) -> None:
    repo_root = tmp_path / "repo"
    skill_root = repo_root / ".codex" / "skills" / "failure-memory"
    lessons_root = repo_root / ".codex" / "lessons"
    records_dir = lessons_root / "records"
    index_path = lessons_root / "index.jsonl"

    records_dir.mkdir(parents=True)
    index_path.write_text("", encoding="utf-8")
    copy_tree(SKILL_DIR, skill_root)

    log_script = skill_root / "scripts" / "log_lesson.py"
    result = subprocess.run(
        [
            sys.executable,
            str(log_script),
            "--type",
            "difficulty",
            "--summary",
            "repo root inference works",
            "--lesson",
            "default repo-root inference should point at the copied repo root",
            "--reusable",
            "yes",
            "--promotion-target",
            "skill",
        ],
        check=True,
        capture_output=True,
        text=True,
    )

    payload = json.loads(result.stdout)
    assert (repo_root / payload["record"]).exists()
    rows = [json.loads(line) for line in index_path.read_text(encoding="utf-8").splitlines() if line]
    assert rows[0]["summary"] == "repo root inference works"


def copy_tree(source: Path, destination: Path) -> None:
    for path in source.rglob("*"):
        target = destination / path.relative_to(source)
        if path.is_dir():
            target.mkdir(parents=True, exist_ok=True)
            continue
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(path.read_bytes())
