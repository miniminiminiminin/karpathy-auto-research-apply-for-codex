import asyncio
from pathlib import Path

from codex_writer.control.uds import DaemonClient
from codex_writer.daemon.server import DaemonServer
from codex_writer.jobs.model import JobItem, JobSpec
from codex_writer.output.write import write_result
from codex_writer.queue.store import create_job, save_job_state, update_item_state


class CountingClient:
    calls = 0

    async def generate(self, prompt: str) -> str:
        type(self).calls += 1
        return f"OUT:{prompt}"


async def _exercise_recovery(tmp_path: Path) -> None:
    runtime_dir = tmp_path / "runtime"
    socket_path = tmp_path / "daemon.sock"
    spec = JobSpec(
        job_id="job-recover",
        prompt_template="Write about {{topic}}.",
        output_dir=tmp_path / "outputs",
        runtime_dir=runtime_dir,
    )
    items = [
        JobItem.from_dict({"filename": "post-1.md", "topic": "done"}),
        JobItem.from_dict({"filename": "post-2.md", "topic": "pending"}),
    ]
    job_dir = create_job(spec, items)
    output = write_result(spec.output_dir, "post-1.md", "OUT:Write about done.")
    update_item_state(job_dir, items[0], {"status": "succeeded", "output_path": str(output)})
    save_job_state(
        job_dir,
        {
            "status": "running",
            "item_count": 2,
            "succeeded": 1,
            "failed": 0,
            "cancelled": 0,
            "stop_requested": False,
        },
    )
    server = DaemonServer(runtime_dir=runtime_dir, socket_path=socket_path, client_factory=CountingClient)
    await server.start()
    await asyncio.sleep(0.1)
    status = DaemonClient(socket_path).get_job("job-recover")
    assert status["succeeded"] == 2
    assert CountingClient.calls == 1
    await server.stop()


def test_daemon_server_recovers_unfinished_jobs_on_start(tmp_path: Path) -> None:
    asyncio.run(_exercise_recovery(tmp_path))
