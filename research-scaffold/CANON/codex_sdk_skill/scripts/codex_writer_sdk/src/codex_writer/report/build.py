from datetime import datetime
from pathlib import Path

from codex_writer.queue.store import completed_state_path, job_dir_for, list_job_ids, load_job_spec, load_job_state
from codex_writer.state.journal import read_json


def build_job_report(runtime_dir: Path, job_id: str) -> dict[str, object]:
    job_dir = job_dir_for(runtime_dir, job_id)
    state = _load_state(runtime_dir, job_id, job_dir)
    items = _load_items(runtime_dir, job_id, state)
    counts = _counts(items, state)
    started_at = str(state.get("created_at") or state.get("started_at") or "")
    ended_at = str(state.get("completed_at") or state.get("updated_at") or "")
    tokens_used = int(state.get("tokens_used", sum(int(item.get("tokens_used", 0)) for item in items)))
    completed = counts["succeeded"] + counts["failed"] + counts["cancelled"]
    ratio = 0.0 if not counts["item_count"] else round(completed / counts["item_count"], 3)
    avg = 0.0 if not counts["succeeded"] else round(tokens_used / counts["succeeded"], 2)
    report = {
        "job_id": job_id,
        "status": state.get("status", "queued"),
        "item_count": counts["item_count"],
        "succeeded": counts["succeeded"],
        "failed": counts["failed"],
        "cancelled": counts["cancelled"],
        "running": counts["running"],
        "queued": counts["queued"],
        "stop_requested": bool(state.get("stop_requested", False)),
        "tokens_used": tokens_used,
        "average_tokens_per_completed_item": avg,
        "completion_ratio": ratio,
        "created_at": state.get("created_at"),
        "started_at": state.get("started_at"),
        "updated_at": state.get("updated_at"),
        "completed_at": state.get("completed_at"),
        "elapsed_seconds": _elapsed_seconds(started_at, ended_at),
        "recent_completed": _recent_completed(items),
        "recent_events": _recent_events(job_dir),
    }
    if "output_dir" in state:
        report["output_dir"] = state["output_dir"]
    else:
        report["output_dir"] = str(load_job_spec(job_dir).output_dir)
    return report


def list_job_reports(runtime_dir: Path) -> list[dict[str, object]]:
    return [build_job_report(runtime_dir, job_id) for job_id in list_job_ids(runtime_dir)]


def _load_items(runtime_dir: Path, job_id: str, state: dict[str, object]) -> list[dict[str, object]]:
    if "items" in state:
        return [dict(item) for item in state.get("items", []) if isinstance(item, dict)]
    states_dir = job_dir_for(runtime_dir, job_id) / "item_states"
    if not states_dir.exists():
        return []
    return [read_json(path) | {"filename": path.stem.replace("__", "/")} for path in sorted(states_dir.glob("*.json"))]


def _load_state(runtime_dir: Path, job_id: str, job_dir: Path) -> dict[str, object]:
    completed_path = completed_state_path(runtime_dir, job_id)
    if completed_path.exists():
        return read_json(completed_path)
    return load_job_state(job_dir)


def _counts(items: list[dict[str, object]], state: dict[str, object]) -> dict[str, int]:
    counts = {"item_count": int(state.get("item_count", len(items))), "succeeded": 0, "failed": 0, "cancelled": 0, "running": 0, "queued": 0}
    for item in items:
        status = str(item.get("status", "queued"))
        if status in counts:
            counts[status] += 1
    return counts


def _elapsed_seconds(started_at: str, ended_at: str) -> float:
    if not started_at or not ended_at:
        return 0.0
    return round((datetime.fromisoformat(ended_at) - datetime.fromisoformat(started_at)).total_seconds(), 3)


def _recent_completed(items: list[dict[str, object]]) -> list[dict[str, object]]:
    completed = [item for item in items if item.get("status") == "succeeded"]
    ranked = sorted(completed, key=lambda item: str(item.get("updated_at", "")), reverse=True)
    return [{"filename": item.get("filename"), "tokens_used": int(item.get("tokens_used", 0))} for item in ranked[:3]]


def _recent_events(job_dir: Path) -> list[dict[str, object]]:
    path = job_dir / "events.jsonl"
    if not path.exists():
        return []
    lines = path.read_text(encoding="utf-8").splitlines()[-5:]
    return [read_json_line(line) for line in lines if line.strip()]


def read_json_line(line: str) -> dict[str, object]:
    import json

    return dict(json.loads(line))
