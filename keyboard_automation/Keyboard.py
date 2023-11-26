from typing import Protocol
from abc import abstractmethod
from pynput.keyboard import Controller


class IKeyboard(Protocol):
    @abstractmethod
    def send_keys(self, keys: str):
        raise NotImplementedError

class Keyboard:
    def __init__(self):
        self.keyboard = Controller()

    def send_keys(self, keys: str):
        self.keyboard.type(keys)
