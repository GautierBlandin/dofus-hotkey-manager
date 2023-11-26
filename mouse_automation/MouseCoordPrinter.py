class MouseCoordPrinter:
    def __init__(self):
        self.active: bool = False

    def on_click(self, x, y, button, pressed):
        if not self.active:
            return
        if pressed:
            print(f'x: {x}, y: {y}')

    # This should be used by the controller to enable/disable the mouse coord printer
    def toggle_active(self):
        self.active = not self.active
