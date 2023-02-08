from hotkey.Hotkey import Hotkey


def test_hotkey():
    class Observer:
        def __init__(self):
            self.number_triggered = 0

        def trigger(self):
            self.number_triggered += 1

    all_modifiers = {10, 11, 12, 13}
    all_normal = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    observer = Observer()
    hotkey = Hotkey({10, 11}, {4}, observer.trigger, all_modifiers)

    expected_number_trigger = 0

    hotkey.press(10)
    hotkey.press(11)
    hotkey.press(4)
    expected_number_trigger += 1
    assert observer.number_triggered == expected_number_trigger
    hotkey.release(10)
    hotkey.release(11)
    hotkey.release(4)

    hotkey.press(10)
    hotkey.press(11)
    hotkey.press(12)
    hotkey.press(4)
    assert observer.number_triggered == expected_number_trigger
    hotkey.release(12)
    hotkey.release(11)
    assert observer.number_triggered == expected_number_trigger
    hotkey.release(4)
    hotkey.press(11)
    hotkey.press(4)
    expected_number_trigger += 1
    assert observer.number_triggered == expected_number_trigger


def test_hotkey_from_string():
    hotkey = Hotkey.from_string('<ctrl>+<alt>+a', lambda: None)
    assert hotkey.modifiers == {17, 18}
    assert hotkey.normal == {65}

    hotkey = Hotkey.from_string('<ctrl>+<alt>+<shift>+a', lambda: None)
    assert hotkey.modifiers == {17, 18, 16}
    assert hotkey.normal == {65}

    hotkey = Hotkey.from_string('<shift>+<space>', lambda: None)
    assert hotkey.modifiers == {16}
    assert hotkey.normal == {32}
