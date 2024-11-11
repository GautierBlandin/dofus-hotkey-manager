from typing import Callable

from dofus_window_manager.AbstractDofusWindowManager import AbstractDofusWindowManager
from keyboard_automation.Keyboard import IKeyboard
import time
from pynput.keyboard import Key

class Traveler:
    def __init__(self, dofus_window_manager: AbstractDofusWindowManager, keyboard: IKeyboard):
        self.dofus_window_manager = dofus_window_manager
        self.keyboard = keyboard
        self.suspend_input = None
        self.resume_input = None

    def get_input(self):
        position = input("Enter the position you want to travel to: ")
        command = f"/travel {position}"
        print(f"Sending command: {command}")
        self.send_command(command)

    def send_command(self, command: str):
        if self.suspend_input is not None:
            self.suspend_input()
        characters = self.dofus_window_manager.get_active_characters()
        for character in characters:
            self.dofus_window_manager.focus_character_window(character)
            time.sleep(0.1)
            self.keyboard.enter_chat()
            time.sleep(0.1)
            self.keyboard.send_keys(command)
            time.sleep(0.1)
            self.keyboard.press_enter()
            time.sleep(0.1)
        for character in characters:
            self.dofus_window_manager.focus_character_window(character)
            time.sleep(0.1)
            self.keyboard.press_enter()
            time.sleep(0.3)
        if self.resume_input is not None:
            self.resume_input()
        # Ensure that hotkeys are released
        self.keyboard.release_keys('d')
        self.keyboard.release_keys(Key.ctrl)
        self.keyboard.release_keys(Key.alt)


    def set_suspend_input(self, suspend_input: Callable[[], None]):
        self.suspend_input = suspend_input

    def set_resume_input(self, resume_input: Callable[[], None]):
        self.resume_input = resume_input
