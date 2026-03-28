import asyncio
from pathlib import Path

from codex_writer.control.uds import DaemonClient
from codex_writer.daemon.server import DaemonServer


class SlowClient:
    async def generate(self, prompt: str) -> str:
        await asyncio.sleep(0.05)
        return f"OUT:{prompt}"


async def _exercise_server(tmp_path: Path) -> None:
    socket_path = tmp_path / "daemon.sock"
    server = DaemonServer(
        runtime_dir=tmp_path / "runtime",
        socket_path=socket_path,
        client_factory=SlowClient,
    )
    await server.start()
    client = DaemonClient(socket_path)
    submit = client.request(
        "submit",
        {
            "prompt_template": "Write about {{topic}}.",
            "items": [
                {"filename": "post-1.md", "topic": "one"},
                {"filename": "post-2.md", "topic": "two"},
            ],
            "output_dir": str(tmp_path / "outputs"),
            "concurrency": 1,
        },
    )
    job_id = submit["job_id"]
    client.request("stop", {"job_id": job_id})
    await asyncio.sleep(0.1)
    stopped = client.request("status", {"job_id": job_id})
    assert stopped["stop_requested"] is True
    client.request("resume", {"job_id": job_id})
    await asyncio.sleep(0.15)
    finished = client.request("status", {"job_id": job_id})
    assert finished["succeeded"] >= 1
    assert "completion_ratio" in finished
    listed = client.request("list", {})
    assert listed["jobs"]
    await server.stop()


def test_daemon_server_submits_stops_and_resumes(tmp_path: Path) -> None:
    asyncio.run(_exercise_server(tmp_path))


async def _exercise_pipeline_server(tmp_path: Path) -> None:
    prompt_dir = tmp_path / "prompts"
    prompt_dir.mkdir()
    (prompt_dir / "01.md").write_text("Plan {{topic}}", encoding="utf-8")
    (prompt_dir / "02.md").write_text("Write {{previous_output}}", encoding="utf-8")
    socket_path = tmp_path / "pipeline.sock"
    server = DaemonServer(
        runtime_dir=tmp_path / "runtime-pipeline",
        socket_path=socket_path,
        client_factory=SlowClient,
    )
    await server.start()
    client = DaemonClient(socket_path)
    submit = client.request(
        "submit",
        {
            "pipeline": {
                "name": "book-chapter",
                "mode": "sequential",
                "final_output": "final.md",
                "stages": [
                    {
                        "id": "architect",
                        "prompt_file": str(prompt_dir / "01.md"),
                        "output_file": "01-architect.md",
                        "use_previous_output": False,
                    },
                    {
                        "id": "writer",
                        "prompt_file": str(prompt_dir / "02.md"),
                        "output_file": "02-writer.md",
                        "use_previous_output": True,
                    },
                ],
            },
            "items": [
                {"filename": "chapter-01/final.md", "topic": "규칙"},
            ],
            "output_dir": str(tmp_path / "outputs-pipeline"),
            "concurrency": 1,
        },
    )
    await asyncio.sleep(0.15)
    finished = client.request("status", {"job_id": submit["job_id"]})
    assert finished["succeeded"] == 1
    assert (tmp_path / "outputs-pipeline" / "chapter-01" / "01-architect.md").exists()
    assert (tmp_path / "outputs-pipeline" / "chapter-01" / "final.md").exists()
    await server.stop()


def test_daemon_server_runs_pipeline_jobs(tmp_path: Path) -> None:
    asyncio.run(_exercise_pipeline_server(tmp_path))
