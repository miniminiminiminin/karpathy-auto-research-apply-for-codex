import json
import shutil
from datetime import UTC, datetime
from pathlib import Path
from uuid import uuid4

from codex_writer.jobs.model import JobItem, JobSpec
from codex_writer.state.journal import read_json, write_item_state, write_json


def recover_item_status(status: str) -> str:
    return "queued" if status == "running" else status


def make_job_id() -> str:
    stamp = datetime.now(UTC).strftime("%Y%m%d%H%M%S")
    return f"job-{stamp}-{uuid4().hex[:6]}"


def job_dir_for(runtime_dir: Path, job_id: str) -> Path:
    return runtime_dir / "jobs" / job_id


def create_job(spec: JobSpec, items: list[JobItem]) -> Path:
    job_dir = job_dir_for(spec.runtime_dir, spec.job_id)
    write_json(job_dir / "spec.json", _spec_payload(spec))
    _write_items(job_dir / "items.jsonl", items)
    write_json(job_dir / "state.json", _initial_state(len(items)))
    for item in items:
        write_item_state(job_dir / "item_states", item.filename, {"status": "queued"})
    return job_dir


def load_job_state(job_dir: Path) -> dict[str, object]:
    state_path = job_dir / "state.json"
    if state_path.exists():
        return read_json(state_path)
    return read_json(completed_state_path(job_dir.parent.parent, job_dir.name))


def save_job_state(job_dir: Path, payload: dict[str, object]) -> Path:
    path = job_dir / "state.json"
    current = read_json(path) if path.exists() else {}
    merged = current | payload | {"updated_at": iso_now()}
    return write_json(path, merged)


def load_job_spec(job_dir: Path) -> JobSpec:
    payload = read_json(job_dir / "spec.json")
    return JobSpec(
        job_id=str(payload["job_id"]),
        prompt_template=str(payload.get("prompt_template", "")),
        output_dir=Path(str(payload["output_dir"])),
        runtime_dir=Path(str(payload["runtime_dir"])),
        concurrency=payload.get("concurrency"),
        dry_run=bool(payload.get("dry_run")),
        pipeline=payload.get("pipeline"),
    )


def load_items(job_dir: Path) -> list[JobItem]:
    lines = (job_dir / "items.jsonl").read_text().splitlines()
    return [JobItem.from_dict(json.loads(line)) for line in lines if line.strip()]


def update_item_state(job_dir: Path, item: JobItem, payload: dict[str, object]) -> Path:
    path = _item_state_path(job_dir, item.filename)
    current = read_json(path) if path.exists() else {}
    merged = current | payload | {"updated_at": iso_now()}
    return write_json(path, merged)


def list_job_ids(runtime_dir: Path) -> list[str]:
    jobs_dir = runtime_dir / "jobs"
    completed_dir = runtime_dir / "completed"
    active = [] if not jobs_dir.exists() else [path.name for path in jobs_dir.iterdir() if path.is_dir()]
    finished = [] if not completed_dir.exists() else [path.stem for path in completed_dir.iterdir() if path.is_file()]
    return sorted(set(active + finished))


def load_unfinished_items(job_dir: Path) -> list[JobItem]:
    pending: list[JobItem] = []
    for item in load_items(job_dir):
        payload = read_json(_item_state_path(job_dir, item.filename))
        status = recover_item_status(str(payload.get("status", "queued")))
        if status in {"queued", "cancelled"}:
            pending.append(item)
            update_item_state(job_dir, item, {"status": "queued"})
    return pending


def set_stop_requested(job_dir: Path, requested: bool) -> dict[str, object]:
    state = load_job_state(job_dir)
    state["stop_requested"] = requested
    state["status"] = "stopped" if requested else "queued"
    save_job_state(job_dir, state)
    return state


def summarize_items(job_dir: Path, items: list[JobItem]) -> dict[str, int]:
    counts = {"succeeded": 0, "failed": 0, "cancelled": 0, "queued": 0, "running": 0}
    for item in items:
        payload = read_json(_item_state_path(job_dir, item.filename))
        status = str(payload.get("status", "queued"))
        counts[status] = counts.get(status, 0) + 1
    return counts


def record_completed_job(spec: JobSpec, state: dict[str, object]) -> Path:
    payload = dict(state)
    payload["job_id"] = spec.job_id
    payload["output_dir"] = str(spec.output_dir)
    payload["items"] = _completed_items(spec.runtime_dir, spec.job_id)
    return write_json(completed_state_path(spec.runtime_dir, spec.job_id), payload)


def cleanup_job_dir(job_dir: Path) -> None:
    if job_dir.exists():
        shutil.rmtree(job_dir)


def _initial_state(item_count: int) -> dict[str, object]:
    now = iso_now()
    return {
        "status": "queued",
        "item_count": item_count,
        "succeeded": 0,
        "failed": 0,
        "cancelled": 0,
        "stop_requested": False,
        "created_at": now,
        "updated_at": now,
    }


def _spec_payload(spec: JobSpec) -> dict[str, object]:
    return {
        "job_id": spec.job_id,
        "prompt_template": spec.prompt_template,
        "output_dir": str(spec.output_dir),
        "runtime_dir": str(spec.runtime_dir),
        "concurrency": spec.concurrency,
        "dry_run": spec.dry_run,
        "pipeline": spec.pipeline,
    }


def _write_items(path: Path, items: list[JobItem]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        for item in items:
            payload = {"filename": item.filename, **item.variables}
            handle.write(json.dumps(payload, ensure_ascii=True) + "\n")


def _item_state_path(job_dir: Path, filename: str) -> Path:
    safe_name = filename.replace("/", "__")
    return job_dir / "item_states" / f"{safe_name}.json"


def completed_state_path(runtime_dir: Path, job_id: str) -> Path:
    return runtime_dir / "completed" / f"{job_id}.json"


def _completed_items(runtime_dir: Path, job_id: str) -> list[dict[str, object]]:
    states_dir = job_dir_for(runtime_dir, job_id) / "item_states"
    if not states_dir.exists():
        return []
    items = [read_json(path) | {"filename": path.stem.replace("__", "/")} for path in sorted(states_dir.glob("*.json"))]
    return items


def iso_now() -> str:
    return datetime.now(UTC).isoformat()
