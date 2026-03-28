import asyncio
import threading
from pathlib import Path

from codex_writer.control.uds import DaemonClient
from codex_writer.daemon.server import DaemonServer
from codex_writer.report.build import build_job_report


class FakeHandle:
    def __init__(self, exit_on_terminate: bool) -> None:
        self.pid = 777
        self.returncode = None
        self.exit_on_terminate = exit_on_terminate
        self.terminate_calls = 0
        self.kill_calls = 0

    def is_running(self) -> bool:
        return self.returncode is None

    def terminate(self) -> None:
        self.terminate_calls += 1
        if self.exit_on_terminate:
            self.returncode = -15

    def kill(self) -> None:
        self.kill_calls += 1
        self.returncode = -9


class BlockingClient:
    entered = threading.Event()
    handle: FakeHandle | None = None

    def __init__(self, on_process=None, exit_on_terminate: bool = True) -> None:
        self.on_process = on_process
        self.exit_on_terminate = exit_on_terminate

    async def generate(self, prompt: str) -> str:
        handle = FakeHandle(self.exit_on_terminate)
        type(self).handle = handle
        type(self).entered.set()
        if self.on_process is not None:
            self.on_process(handle)
        while handle.is_running():
            await asyncio.sleep(0.01)
        raise RuntimeError("terminated")


async def _wait_for(predicate, timeout: float = 1.0) -> None:
    deadline = asyncio.get_running_loop().time() + timeout
    while not predicate():
        if asyncio.get_running_loop().time() >= deadline:
            raise TimeoutError("condition was not met")
        await asyncio.sleep(0.01)


async def _submit_job(tmp_path: Path, factory) -> tuple[DaemonServer, str]:
    BlockingClient.entered = threading.Event()
    BlockingClient.handle = None
    socket_path = tmp_path / "daemon.sock"
    server = DaemonServer(tmp_path / "runtime", socket_path, client_factory=factory)
    await server.start()
    job_id = DaemonClient(socket_path).request(
        "submit",
        {
            "prompt_template": "Write about {{topic}}.",
            "items": [{"filename": "post-1.md", "topic": "one"}],
            "output_dir": str(tmp_path / "outputs"),
            "concurrency": 1,
        },
    )["job_id"]
    await _wait_for(lambda: BlockingClient.entered.is_set())
    return server, job_id


async def _exercise_job_stop_cleanup(tmp_path: Path) -> None:
    server, job_id = await _submit_job(tmp_path, lambda on_process=None: BlockingClient(on_process, True))
    client = DaemonClient(tmp_path / "daemon.sock")
    client.request("stop", {"job_id": job_id})
    await _wait_for(lambda: build_job_report(tmp_path / "runtime", job_id)["cancelled"] == 1)
    handle = BlockingClient.handle
    assert handle is not None
    assert handle.terminate_calls == 1
    assert handle.kill_calls == 0
    await server.stop()


async def _exercise_server_shutdown_cleanup(tmp_path: Path) -> None:
    server, job_id = await _submit_job(tmp_path, lambda on_process=None: BlockingClient(on_process, False))
    await server.stop()
    report = build_job_report(tmp_path / "runtime", job_id)
    handle = BlockingClient.handle
    assert handle is not None
    assert handle.terminate_calls == 1
    assert handle.kill_calls == 1
    assert report["cancelled"] == 1
    assert report["stop_requested"] is True


def test_daemon_stop_terminates_active_job_process(tmp_path: Path) -> None:
    asyncio.run(_exercise_job_stop_cleanup(tmp_path))


def test_daemon_shutdown_kills_stubborn_active_process(tmp_path: Path) -> None:
    asyncio.run(_exercise_server_shutdown_cleanup(tmp_path))
