import threading
from dataclasses import dataclass, field
from time import monotonic, sleep

from codex_writer.stop.token import StopToken

STOP_WAIT_SECONDS = 0.2


@dataclass(slots=True)
class JobRuntime:
    thread: threading.Thread
    token: StopToken
    handles: list[object] = field(default_factory=list)
    lock: threading.Lock = field(default_factory=threading.Lock)

    def add_handle(self, handle: object) -> None:
        with self.lock:
            self.handles.append(handle)

    def active_handles(self) -> list[object]:
        with self.lock:
            self.handles = [handle for handle in self.handles if handle.is_running()]
            return list(self.handles)


def stop_handles(handles: list[object], timeout: float = STOP_WAIT_SECONDS) -> None:
    for handle in handles:
        handle.terminate()
    _wait_for_exit(handles, timeout)
    for handle in handles:
        if handle.is_running():
            handle.kill()
    _wait_for_exit(handles, timeout)


def _wait_for_exit(handles: list[object], timeout: float) -> None:
    deadline = monotonic() + timeout
    while monotonic() < deadline:
        if not any(handle.is_running() for handle in handles):
            return
        sleep(0.01)
