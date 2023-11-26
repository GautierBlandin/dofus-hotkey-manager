from dofus_window_manager.AbstractDofusWindowManager import AbstractDofusWindowManager
from keyboard_automation.Keyboard import IKeyboard
import time

class Traveler:
    def __init__(self, dofus_window_manager: AbstractDofusWindowManager, keyboard: IKeyboard):
        self.dofus_window_manager = dofus_window_manager
        self.keyboard = keyboard

    def get_input(self):
        position = input("Enter the position you want to travel to: ")
        command = f"/travel {position}"
        print(f"Sending command: {command}")
        self.send_command(command)

    def send_command(self, command: str):
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
