from pathlib import Path

from codex_writer.jobs.model import JobSpec
from codex_writer.queue.store import load_job_state, record_completed_job


def test_record_completed_job_keeps_status_after_cleanup(tmp_path: Path) -> None:
    runtime_dir = tmp_path / "runtime"
    spec = JobSpec("job-1", "Write", tmp_path / "outputs", runtime_dir)
    state = {"status": "completed", "item_count": 1, "succeeded": 1}
    record_completed_job(spec, state)
    completed = runtime_dir / "completed" / "job-1.json"
    assert completed.exists()
    assert load_job_state(completed.parent / "job-1")["status"] == "completed"
