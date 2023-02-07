import os

from hotkey_managers.smithmagic_manager.SmithmagicManager import SmithmagicManager, IMouse


class StubMouse(IMouse):
    def __init__(self):
        self.x = None
        self.y = None
        self.clicked: list[tuple[int, int]] = []

    def click(self, x, y):
        self.x = x
        self.y = y
        self.clicked.append((x, y))


def test_smithmagic_manager():
    script_dir = os.path.dirname(__file__)
    rel_path = './smithmagic_test_configuration.yaml'
    abs_file_path = os.path.join(script_dir, rel_path)
    mouse = StubMouse()

    smithmagic_manager = SmithmagicManager.create_from_yaml(abs_file_path, mouse)

    hotkey_dict = smithmagic_manager.create_hotkey_dictionary()

    hotkey_dict['<alt>+<ctrl>+m']()
    hotkey_dict['q']()
    assert mouse.x == 1
    assert mouse.y == 1
    hotkey_dict['<shift>+q']()
    assert mouse.x == 2
    assert mouse.y == 1
    hotkey_dict['<ctrl>+q']()
    assert mouse.x == 3
    assert mouse.y == 1
    hotkey_dict['<space>']()
    assert mouse.x == 100
    assert mouse.y == 200
    hotkey_dict['<shift>+<ctrl>+<space>']()
    assert mouse.x == 1000
    assert mouse.y == 2000
    hotkey_dict['<alt>+<ctrl>+m']()
    hotkey_dict['<space>']()
    assert mouse.x == 1000
    assert mouse.y == 2000
