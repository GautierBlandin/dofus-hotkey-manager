from typing import Callable
import keycode


class Hotkey:
    def __init__(self, modifiers: set[int], normal: set[int], on_trigger: Callable[[], None], all_modifiers: set[int]):
        self.modifiers = modifiers
        self.normal = normal
        self.on_trigger = on_trigger
        self.all_modifiers = all_modifiers
        self.pressed_modifiers: set[int] = set()
        self.pressed_normal: set[int] = set()

    @staticmethod
    def from_string(string: str, on_trigger: Callable[[], None]):
        modifiers = set()
        normal = set()
        for key in string.split('+'):
            if len(key) == 1:
                num_key = keycode.keycodes[key]
            elif key[0] == '<' and key[-1] == '>':
                num_key = keycode.keycodes[key[1:-1]]
            else:
                raise ValueError(f'Invalid key: {key}. Check the documentation for valid keys.')
            if num_key in keycode.normalizer:
                num_key = keycode.normalizer[key]
            if num_key in keycode.modifiers:
                modifiers.add(num_key)
            else:
                normal.add(num_key)
        return Hotkey(modifiers, normal, on_trigger, keycode.modifiers)

    def press(self, key: int):
        if key in self.all_modifiers:
            self.pressed_modifiers.add(key)
        else:
            self.pressed_normal.add(key)
            if self.pressed_modifiers == self.modifiers and self.pressed_normal == self.normal:
                self.on_trigger()

    def release(self, key: int):
        if key in self.all_modifiers:
            if key in self.pressed_modifiers:
                self.pressed_modifiers.remove(key)
        else:
            if key in self.pressed_normal:
                self.pressed_normal.remove(key)
