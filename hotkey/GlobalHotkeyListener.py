from pynput.keyboard import Listener, Key, KeyCode
from typing import Callable

from hotkey.Hotkey import Hotkey
import keycode


class GlobalHotkeyListener(Listener):
    def __init__(self, hotkey_dict: dict[str, Callable[[], None]]):
        self.hotkeys = self.parse_dict(hotkey_dict)
        self.input_suspended = False
        super().__init__(on_press=self.on_press, on_release=self.on_release)

    @staticmethod
    def parse_dict(hotkey_dict: dict[str, Callable[[], None]]):
        hotkeys = []
        for hotkey_string, on_trigger in hotkey_dict.items():
            hotkeys.append(Hotkey.from_string(hotkey_string, on_trigger))
        return hotkeys

    @staticmethod
    def key_to_vk(key):
        if isinstance(key, Key):
            return key.value.vk
        elif isinstance(key, KeyCode):
            return int(key.vk)
        else:
            raise ValueError(f'Unknown key type: {type(key)}')

    @staticmethod
    def preprocess_key(key):
        vk = GlobalHotkeyListener.key_to_vk(key)
        if vk in keycode.normalizer:
            vk = keycode.normalizer[vk]
        return vk

    def on_press(self, key):
        if self.input_suspended:
            return
        vk = self.preprocess_key(key)
        print(f'Pressed: {key}')
        for hotkey in self.hotkeys:
            hotkey.press(vk)

    def on_release(self, key):
        if self.input_suspended:
            return
        vk = self.preprocess_key(key)
        print(f'Released: {key}')
        for hotkey in self.hotkeys:
            hotkey.release(vk)

    def suspend_input(self):
        print('Keyboard Input suspended')
        self.input_suspended = True

    def resume_input(self):
        print('Keyboard Input resumed')
        self.input_suspended = False
