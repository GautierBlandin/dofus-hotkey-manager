import pynput
import time
import pythoncom
import win32api, win32con

from dofus_window_manager.AbstractDofusWindowManager import AbstractDofusWindowManager


def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)


def right_click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, x, y, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, x, y, 0, 0)


class MouseRepeater:
    def __init__(self, dofus_window_manager: AbstractDofusWindowManager, repeat_interval: float = 0.1):
        self.dofus_window_manager = dofus_window_manager
        self.controller = pynput.mouse.Controller()
        self.active: bool = False
        self.clicking: bool = False
        self.repeat_interval: float = 0.1

    def set_active(self):
        self.active = True

    def set_inactive(self):
        self.active = False

    def toggle_active(self):
        self.active = not self.active

    def toggle_clicking(self):
        self.clicking = not self.clicking

    def set_clicking(self, clicking: bool):
        self.clicking = clicking

    def repeat_click_all_active_characters(self, x: int, y: int, button: pynput.mouse.Button, count: int):
        self.set_clicking(True)
        time.sleep(0.5)
        for i in range(len(self.dofus_window_manager.get_active_characters()) - 1):
            time.sleep(self.repeat_interval)
            self.dofus_window_manager.focus_next_character_window()
            time.sleep(0.1)
            print(f'hello {x} {y}')
            if button == pynput.mouse.Button.left:
                click(x, y)
            elif button == pynput.mouse.Button.right:
                right_click(x, y)
        time.sleep(self.repeat_interval)
        self.dofus_window_manager.focus_next_character_window()
        self.set_clicking(False)

    def on_click(self, x, y, button, pressed):
        if self.clicking:
            return
        pythoncom.CoInitialize()
        if not self.active:
            return
        if not pressed:
            self.repeat_click_all_active_characters(x, y, button, 1)
