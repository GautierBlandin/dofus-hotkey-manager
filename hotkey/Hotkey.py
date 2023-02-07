from typing import Callable


class Hotkey:
    def __init__(self, modifiers: set[int], normal: set[int], on_trigger: Callable[[], None], all_modifiers: set[int],
                 all_normal: set[int]):
        self.modifiers = modifiers
        self.normal = normal
        self.on_trigger = on_trigger
        self.all_modifiers = all_modifiers
        self.all_normal = all_normal
        self.pressed_modifiers: set[int] = set()
        self.pressed_normal: set[int] = set()

    def press(self, key: int):
        if key in self.all_modifiers:
            self.pressed_modifiers.add(key)
        if key in self.all_normal:
            self.pressed_normal.add(key)
            if self.pressed_modifiers == self.modifiers and self.pressed_normal == self.normal:
                self.on_trigger()

    def release(self, key: int):
        if key in self.all_modifiers:
            self.pressed_modifiers.remove(key)
        if key in self.all_normal:
            self.pressed_normal.remove(key)
