import json
from pathlib import Path

from codex_writer.jobs.model import JobItem, JobSpec
from codex_writer.output.write import write_result
from codex_writer.queue.store import create_job, record_completed_job, save_job_state, update_item_state
from codex_writer.report.build import build_job_report


def test_build_job_report_for_running_job(tmp_path: Path) -> None:
    runtime_dir = tmp_path / "runtime"
    spec = JobSpec("job-1", "Write", tmp_path / "outputs", runtime_dir)
    items = [
        JobItem.from_dict({"filename": "a.md", "topic": "one"}),
        JobItem.from_dict({"filename": "b.md", "topic": "two"}),
    ]
    job_dir = create_job(spec, items)
    output = write_result(spec.output_dir, "a.md", "OUT")
    update_item_state(job_dir, items[0], {"status": "succeeded", "tokens_used": 20, "output_path": str(output)})
    update_item_state(job_dir, items[1], {"status": "running"})
    save_job_state(
        job_dir,
        {
            "status": "running",
            "item_count": 2,
            "succeeded": 1,
            "failed": 0,
            "cancelled": 0,
            "stop_requested": False,
            "created_at": "2026-03-09T12:00:00+00:00",
            "started_at": "2026-03-09T12:00:01+00:00",
            "updated_at": "2026-03-09T12:01:00+00:00",
            "tokens_used": 20,
        },
    )
    report = build_job_report(runtime_dir, "job-1")
    assert report["running"] == 1
    assert report["queued"] == 0
    assert report["completion_ratio"] == 0.5
    assert report["average_tokens_per_completed_item"] == 20.0
    assert report["recent_completed"][0]["filename"] == "a.md"


def test_build_job_report_for_completed_job(tmp_path: Path) -> None:
    runtime_dir = tmp_path / "runtime"
    spec = JobSpec("job-2", "Write", tmp_path / "outputs", runtime_dir)
    state = {
        "status": "completed",
        "item_count": 1,
        "succeeded": 1,
        "failed": 0,
        "cancelled": 0,
        "stop_requested": False,
        "created_at": "2026-03-09T12:00:00+00:00",
        "started_at": "2026-03-09T12:00:01+00:00",
        "updated_at": "2026-03-09T12:01:00+00:00",
        "completed_at": "2026-03-09T12:02:00+00:00",
        "tokens_used": 33,
    }
    job_dir = create_job(spec, [JobItem.from_dict({"filename": "a.md", "topic": "one"})])
    update_item_state(job_dir, JobItem.from_dict({"filename": "a.md", "topic": "one"}), {"status": "succeeded", "tokens_used": 33})
    record_completed_job(spec, state)
    report = build_job_report(runtime_dir, "job-2")
    assert report["status"] == "completed"
    assert report["elapsed_seconds"] == 120.0
    assert report["tokens_used"] == 33
