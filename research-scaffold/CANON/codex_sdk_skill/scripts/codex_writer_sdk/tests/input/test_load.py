import json
from pathlib import Path

from codex_writer.input.load import load_items


def test_load_items_reads_jsonl(tmp_path: Path) -> None:
    path = tmp_path / "items.jsonl"
    path.write_text(json.dumps({"filename": "post-1.md", "topic": "AI"}) + "\n")
    items = load_items(path)
    assert items[0].filename == "post-1.md"
    assert items[0].variables["topic"] == "AI"
