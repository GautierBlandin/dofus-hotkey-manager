from typing import Protocol
from abc import abstractmethod
from pynput.keyboard import Controller, Key


class IKeyboard(Protocol):
    @abstractmethod
    def send_keys(self, keys: str):
        raise NotImplementedError

    @abstractmethod
    def press_enter(self):
        raise NotImplementedError

    @abstractmethod
    def enter_chat(self):
        raise NotImplementedError

    @abstractmethod
    def release_keys(self, key: str | Key):
        raise NotImplementedError

class Keyboard:
    def __init__(self):
        self.keyboard = Controller()

    def send_keys(self, keys: str):
        print(f"Sending keys: {keys}")
        self.keyboard.type(keys)

    def release_keys(self, key: str | Key):
        self.keyboard.release(key)

    def press_enter(self):
        self.keyboard.press(Key.enter)
        self.keyboard.release(Key.enter)

    def enter_chat(self):
        self.keyboard.press(Key.tab)
        self.keyboard.release(Key.tab)
