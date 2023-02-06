class Suspender:
    def __init__(self):
        self.suspended = False

    def toggle_suspended(self):
        self.suspended = not self.suspended

    def set_suspended(self, suspended: bool):
        self.suspended = suspended

    def make_suspendable(self, function):
        def suspended(*args, **kwargs):
            if not self.suspended:
                return function(*args, **kwargs)

        return suspended
