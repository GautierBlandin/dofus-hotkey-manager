import win32api
import win32con
from typing import Protocol
from abc import abstractmethod

class IMouse(Protocol):
    @abstractmethod
    def click(self, x: int, y: int):
        raise NotImplementedError

    @abstractmethod
    def right_click(self, x: int, y: int):
        raise NotImplementedError


class Mouse:
    def click(self, x, y):
        win32api.SetCursorPos((x, y))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)


    def right_click(self, x, y):
        win32api.SetCursorPos((x, y))
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, x, y, 0, 0)
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, x, y, 0, 0)
