import json
from pathlib import Path

from codex_writer.jobs.model import JobItem


def load_items(path: Path) -> list[JobItem]:
    if path.suffix == ".json":
        payload = json.loads(path.read_text())
        return [JobItem.from_dict(item) for item in payload]
    if path.suffix == ".jsonl":
        lines = [line for line in path.read_text().splitlines() if line.strip()]
        return [JobItem.from_dict(json.loads(line)) for line in lines]
    raise ValueError(f"Unsupported input format: {path.suffix}")
