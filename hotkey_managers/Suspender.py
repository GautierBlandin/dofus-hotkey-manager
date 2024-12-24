from typing import Callable


class Suspender:
    def __init__(self, suspended=False):
        self.suspended = suspended

    def toggle_suspended(self) -> None:
        next_suspended_state = not self.suspended
        if next_suspended_state:
            print('Hotkeys are now suspended')
        else:
            print('Hotkeys are now active')
        self.suspended = not self.suspended

    def set_suspended(self, suspended: bool) -> None:
        self.suspended = suspended

    def make_suspendable(self, function) -> Callable:
        def suspended(*args, **kwargs):
            if not self.suspended:
                return function(*args, **kwargs)

        return suspended
