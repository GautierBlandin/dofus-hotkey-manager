from typing import Callable


class Suspender:
    def __init__(self, suspended=False):
        self.suspended = suspended

    def toggle_suspended(self) -> None:
        self.suspended = not self.suspended

    def set_suspended(self, suspended: bool) -> None:
        self.suspended = suspended

    def make_suspendable(self, function) -> Callable:
        def suspended(*args, **kwargs):
            if not self.suspended:
                return function(*args, **kwargs)

        return suspended
