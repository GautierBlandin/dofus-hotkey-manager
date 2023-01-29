import logging
from typing import Callable

import pythoncom


from process_manager.AbstractProcessManager import AbstractProcessManager
from process_manager.ProcessManager import ProcessManager
from dofus_window_manager.AbstractDofusWindowManager import AbstractDofusWindowManager


class DofusWindowManager(AbstractDofusWindowManager):
    """
    Class to manage Dofus windows

    Attributes:
        dofus_window_handles: dict[str, int]:
            Dictionary of Dofus window handles, initialized with init_dofus_window_handles
        process_manager: ProcessManager:
            Process manager object that allows access to the system's processes and windows

    Methods:
        init_dofus_window_handles(character_names: list[str]) -> None:
            Initializes the dofus_window_handles attribute
        focus_character_window(character_name: str) -> None:
            Focuses the window of the character with the given name
    """

    def __init__(self, character_names: list[str], process_manager: AbstractProcessManager = ProcessManager()):
        self.dofus_window_handles = None
        self.process_manager = process_manager
        self.character_names = character_names
        self.last_focus = 0
        self.character_to_index = {character_names[i]: i for i in range(len(character_names))}
        self.index_to_character = {i: character_names[i] for i in range(len(character_names))}
        self.number_of_characters = len(character_names)

    def init_dofus_window_handles(self) -> None:
        pythoncom.CoInitialize()
        process_list = self.process_manager.get_process_ids_by_name("Dofus.exe")
        dofus_window_handles = {}
        for character_name in self.character_names:
            hwnd = self.process_manager.get_window_handle_from_title(character_name, process_list)
            if hwnd is not None:
                print(f'Found window: {hwnd}')
            dofus_window_handles[character_name] = hwnd
        self.dofus_window_handles = dofus_window_handles

    def focus_character_window(self, character_name: str) -> None:
        if self.dofus_window_handles[character_name] is None:
            logging.error(f'Character {character_name} window not found')
        else:
            self.process_manager.set_foreground_window(self.dofus_window_handles[character_name])
            self.last_focus = self.character_to_index[character_name]

    def focus_character_window_maker(self, character_name: str) -> Callable[[], None]:
        def focus_character_window_instance() -> None:
            self.focus_character_window(character_name)
        return focus_character_window_instance

    def is_character_handle_defined(self, character_name: str) -> bool:
        return self.dofus_window_handles[character_name] is not None

    def get_next_defined_character(self, character_name: str) -> str:
        index = (self.character_to_index[character_name] + 1) % self.number_of_characters
        safety_counter = 0
        while not self.is_character_handle_defined(self.index_to_character[index]):
            safety_counter += 1
            if safety_counter > self.number_of_characters + 1:
                raise Exception(f'No defined character found for {character_name}')
            index = (index + 1) % self.number_of_characters
        return self.index_to_character[index]

    def get_previous_defined_character(self, character_name: str) -> str:
        index = (self.character_to_index[character_name] - 1) % self.number_of_characters
        safety_counter = 0
        while not self.is_character_handle_defined(self.index_to_character[index]):
            safety_counter += 1
            if safety_counter > self.number_of_characters + 1:
                raise Exception(f'No defined character found for {character_name}')
            index = (index - 1) % self.number_of_characters
        return self.index_to_character[index]

    def focus_next_character_window(self) -> None:
        next_character = self.get_next_defined_character(self.index_to_character[self.last_focus])
        self.last_focus = self.character_to_index[next_character]

        self.focus_character_window(self.index_to_character[self.last_focus])

    def focus_previous_character_window(self) -> None:
        previous_character = self.get_previous_defined_character(self.index_to_character[self.last_focus])
        self.last_focus = self.character_to_index[previous_character]

        self.focus_character_window(self.index_to_character[self.last_focus])
