import json
import socket
from hashlib import sha1
from pathlib import Path


def encode_request(command: str, payload: dict[str, object] | None = None) -> bytes:
    body = {"command": command, "payload": payload or {}}
    return (json.dumps(body, ensure_ascii=True) + "\n").encode()


def decode_message(data: bytes) -> dict[str, object]:
    return json.loads(data.decode().strip() or "{}")


def resolve_socket_path(socket_path: Path) -> Path:
    raw = str(socket_path)
    if len(raw) < 90:
        return socket_path
    digest = sha1(raw.encode()).hexdigest()[:12]
    return Path("/tmp") / f"codex-writer-{digest}.sock"


class DaemonClient:
    def __init__(self, socket_path: Path) -> None:
        self.socket_path = resolve_socket_path(socket_path)

    def request(self, command: str, payload: dict[str, object] | None = None) -> dict[str, object]:
        with socket.socket(socket.AF_UNIX, socket.SOCK_STREAM) as conn:
            conn.connect(str(self.socket_path))
            conn.sendall(encode_request(command, payload))
            conn.shutdown(socket.SHUT_WR)
            chunks: list[bytes] = []
            while True:
                data = conn.recv(65536)
                if not data:
                    break
                chunks.append(data)
        response = decode_message(b"".join(chunks))
        if response.get("ok") is False:
            raise RuntimeError(str(response.get("error", "daemon request failed")))
        return dict(response.get("data", {}))

    def submit_job(self, payload: dict[str, object]) -> dict[str, object]:
        return self.request("submit", payload)

    def get_job(self, job_id: str) -> dict[str, object]:
        return self.request("status", {"job_id": job_id})

    def report_job(self, job_id: str) -> dict[str, object]:
        return self.request("report", {"job_id": job_id})

    def stop_job(self, job_id: str) -> dict[str, object]:
        return self.request("stop", {"job_id": job_id})

    def resume_job(self, job_id: str) -> dict[str, object]:
        return self.request("resume", {"job_id": job_id})
