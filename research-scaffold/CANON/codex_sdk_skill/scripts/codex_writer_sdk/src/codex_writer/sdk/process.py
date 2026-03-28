class ActiveProcess:
    def __init__(self, process: object) -> None:
        self._process = process
        self._closed = False

    @property
    def pid(self) -> int | None:
        value = getattr(self._process, "pid", None)
        return value if isinstance(value, int) else None

    def is_running(self) -> bool:
        return not self._closed and getattr(self._process, "returncode", None) is None

    def terminate(self) -> None:
        if self.is_running():
            self._process.terminate()

    def kill(self) -> None:
        if self.is_running():
            self._process.kill()

    def close(self) -> None:
        self._closed = True
