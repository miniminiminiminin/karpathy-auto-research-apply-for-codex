import json
from uuid import uuid4
from pathlib import Path


def append_jsonl(path: Path, payload: dict[str, object]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(payload, ensure_ascii=True) + "\n")


def write_json(path: Path, payload: dict[str, object]) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    temp_path = path.with_name(f".{path.name}.{uuid4().hex}.tmp")
    temp_path.write_text(json.dumps(payload, ensure_ascii=True, indent=2), encoding="utf-8")
    temp_path.replace(path)
    return path


def read_json(path: Path) -> dict[str, object]:
    return json.loads(path.read_text())


def write_item_state(base_dir: Path, filename: str, payload: dict[str, object]) -> Path:
    safe_name = filename.replace("/", "__")
    return write_json(base_dir / f"{safe_name}.json", payload)
