from pynput.keyboard import Listener, Key, KeyCode
from typing import Callable

from hotkey.Hotkey import Hotkey
import keycode


class GlobalHotkeyListener(Listener):
    def __init__(self, hotkey_dict: dict[str, Callable[[], None]]):
        self.hotkeys = self.parse_dict(hotkey_dict)
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
        vk = self.preprocess_key(key)
        for hotkey in self.hotkeys:
            hotkey.press(vk)

    def on_release(self, key):
        vk = self.preprocess_key(key)
        for hotkey in self.hotkeys:
            hotkey.release(vk)
