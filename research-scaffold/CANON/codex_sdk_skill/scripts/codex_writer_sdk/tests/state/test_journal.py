import json
from pathlib import Path

from codex_writer.state.journal import append_jsonl, write_item_state


def test_append_jsonl_writes_records(tmp_path: Path) -> None:
    path = tmp_path / "events.jsonl"
    append_jsonl(path, {"event": "queued"})
    lines = path.read_text().splitlines()
    assert json.loads(lines[0])["event"] == "queued"


def test_write_item_state_persists_json(tmp_path: Path) -> None:
    path = write_item_state(tmp_path, "post-1.md", {"status": "queued"})
    assert json.loads(path.read_text())["status"] == "queued"
