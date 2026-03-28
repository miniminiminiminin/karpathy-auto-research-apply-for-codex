import asyncio
import inspect
import json
import socketserver
import threading
from pathlib import Path

from codex_writer.control.uds import resolve_socket_path
from codex_writer.daemon.runtime import JobRuntime, stop_handles
from codex_writer.jobs.model import JobItem, JobSpec
from codex_writer.queue.store import (
    create_job,
    job_dir_for,
    list_job_ids,
    load_job_spec,
    load_unfinished_items,
    make_job_id,
    set_stop_requested,
)
from codex_writer.report.build import build_job_report, list_job_reports
from codex_writer.runner.batch import run_batch
from codex_writer.sdk.client import CodexClient
from codex_writer.stop.token import StopToken


class DaemonServer:
    def __init__(self, runtime_dir: Path, socket_path: Path, client_factory: type | None = None) -> None:
        self.runtime_dir = runtime_dir
        self.socket_path = resolve_socket_path(socket_path)
        self.client_factory = client_factory or CodexClient
        self._jobs: dict[str, JobRuntime] = {}
        self._lock = threading.Lock()
        self._server: socketserver.ThreadingUnixStreamServer | None = None
        self._thread: threading.Thread | None = None

    async def start(self) -> None:
        self.socket_path.parent.mkdir(parents=True, exist_ok=True)
        if self.socket_path.exists():
            self.socket_path.unlink()
        self._server = _build_server(self.socket_path, self._handle_request)
        self._thread = threading.Thread(target=self._server.serve_forever, daemon=True)
        self._thread.start()
        self._recover_jobs()

    async def stop(self) -> None:
        if self._server is not None:
            self._server.shutdown()
            self._server.server_close()
        with self._lock:
            job_ids = list(self._jobs)
        for job_id in job_ids:
            self._stop_job(job_id)
        if self.socket_path.exists():
            self.socket_path.unlink()

    def _handle_request(self, command: str, payload: dict[str, object]) -> dict[str, object]:
        return getattr(self, f"_cmd_{command}")(payload)

    def _cmd_submit(self, payload: dict[str, object]) -> dict[str, object]:
        job_id = make_job_id()
        items = [JobItem.from_dict(item) for item in payload["items"]]
        spec = JobSpec(
            job_id=job_id,
            prompt_template=str(payload.get("prompt_template", "")),
            output_dir=Path(str(payload["output_dir"])),
            runtime_dir=self.runtime_dir,
            concurrency=payload.get("concurrency"),
            dry_run=bool(payload.get("dry_run", False)),
            pipeline=payload.get("pipeline"),
        )
        job_dir = create_job(spec, items)
        self._launch_job(spec, items, job_dir)
        return {"job_id": job_id}

    def _cmd_status(self, payload: dict[str, object]) -> dict[str, object]:
        return build_job_report(self.runtime_dir, str(payload["job_id"]))

    def _cmd_list(self, payload: dict[str, object]) -> dict[str, object]:
        return {"jobs": list_job_reports(self.runtime_dir)}

    def _cmd_report(self, payload: dict[str, object]) -> dict[str, object]:
        return build_job_report(self.runtime_dir, str(payload["job_id"]))

    def _cmd_stop(self, payload: dict[str, object]) -> dict[str, object]:
        job_id = str(payload["job_id"])
        self._stop_job(job_id)
        return set_stop_requested(job_dir_for(self.runtime_dir, job_id), True)

    def _cmd_resume(self, payload: dict[str, object]) -> dict[str, object]:
        job_id = str(payload["job_id"])
        job_dir = job_dir_for(self.runtime_dir, job_id)
        if self._is_running(job_id):
            return {"job_id": job_id, "queued": 0, "running": True}
        spec = load_job_spec(job_dir)
        items = load_unfinished_items(job_dir)
        set_stop_requested(job_dir, False)
        if items:
            self._launch_job(spec, items, job_dir)
        return {"job_id": job_id, "queued": len(items)}

    def _launch_job(self, spec: JobSpec, items: list[JobItem], job_dir: Path) -> None:
        if self._is_running(spec.job_id):
            return
        token = StopToken()
        thread = threading.Thread(target=self._run_job, args=(spec, items, token, job_dir), daemon=True)
        with self._lock:
            self._jobs[spec.job_id] = JobRuntime(thread=thread, token=token)
        thread.start()

    def _recover_jobs(self) -> None:
        for job_id in list_job_ids(self.runtime_dir):
            job_dir = job_dir_for(self.runtime_dir, job_id)
            state = build_job_report(self.runtime_dir, job_id)
            if state.get("status") == "completed" or state.get("stop_requested"):
                continue
            items = load_unfinished_items(job_dir)
            if not items:
                continue
            self._launch_job(load_job_spec(job_dir), items, job_dir)

    def _run_job(self, spec: JobSpec, items: list[JobItem], token: StopToken, job_dir: Path) -> None:
        try:
            asyncio.run(run_batch(spec, items, self._build_client(spec.job_id), token, job_dir))
        finally:
            with self._lock:
                current = self._jobs.get(spec.job_id)
                if current is not None and current.thread is threading.current_thread():
                    self._jobs.pop(spec.job_id, None)

    def _is_running(self, job_id: str) -> bool:
        with self._lock:
            job = self._jobs.get(job_id)
        if job is None:
            return False
        return job.thread.is_alive()

    def _build_client(self, job_id: str) -> object:
        signature = inspect.signature(self.client_factory)
        if "on_process" not in signature.parameters:
            return self.client_factory()
        return self.client_factory(on_process=lambda handle: self._register_handle(job_id, handle))

    def _register_handle(self, job_id: str, handle: object) -> None:
        with self._lock:
            runtime = self._jobs.get(job_id)
        if runtime is not None:
            runtime.add_handle(handle)

    def _stop_job(self, job_id: str) -> None:
        with self._lock:
            runtime = self._jobs.get(job_id)
        if runtime is None:
            return
        set_stop_requested(job_dir_for(self.runtime_dir, job_id), True)
        runtime.token.request_stop()
        stop_handles(runtime.active_handles())
        runtime.thread.join(timeout=1)


def _build_server(
    socket_path: Path,
    handler: callable,
) -> socketserver.ThreadingUnixStreamServer:
    class RequestHandler(socketserver.StreamRequestHandler):
        def handle(self) -> None:
            raw = self.rfile.readline()
            try:
                payload = json.loads(raw.decode())
                data = handler(str(payload["command"]), dict(payload.get("payload", {})))
                body = {"ok": True, "data": data}
            except Exception as exc:
                body = {"ok": False, "error": str(exc)}
            self.wfile.write((json.dumps(body, ensure_ascii=True) + "\n").encode())

    return socketserver.ThreadingUnixStreamServer(str(socket_path), RequestHandler)
