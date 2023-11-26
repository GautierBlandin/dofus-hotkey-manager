import pynput
import time
import pythoncom
from mouse_automation.mouse.Mouse import IMouse

from dofus_window_manager.AbstractDofusWindowManager import AbstractDofusWindowManager

class MouseRepeater:
    def __init__(self, dofus_window_manager: AbstractDofusWindowManager, mouse: IMouse, repeat_interval: float = 0.1):
        self.dofus_window_manager = dofus_window_manager
        self.active: bool = False
        self.clicking: bool = False
        self.repeat_interval: float = repeat_interval
        self.mouse = mouse

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
            if button == pynput.mouse.Button.left:
                self.mouse.click(x, y)
            elif button == pynput.mouse.Button.right:
                self.mouse.right_click(x, y)
        time.sleep(self.repeat_interval)
        self.dofus_window_manager.focus_next_character_window()
        self.set_clicking(False)

    def on_click(self, x, y, button, pressed):
        if self.clicking:
            return
        # Ensure pythoncom is initialized in the current thread before
        pythoncom.CoInitialize()
        if not self.active:
            return
        if not pressed:
            self.repeat_click_all_active_characters(x, y, button, 1)
