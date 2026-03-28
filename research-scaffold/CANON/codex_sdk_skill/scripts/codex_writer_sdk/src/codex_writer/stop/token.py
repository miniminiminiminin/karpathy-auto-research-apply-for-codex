class StopToken:
    def __init__(self) -> None:
        self._requested = False

    @property
    def requested(self) -> bool:
        return self._requested

    def request_stop(self) -> None:
        self._requested = True
