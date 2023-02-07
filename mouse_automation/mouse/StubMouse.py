class StubMouse:
    def click(self, x, y):
        print(f'clicked ({x}, {y})')

    def right_click(self, x, y):
        print(f'right clicked ({x}, {y})')
