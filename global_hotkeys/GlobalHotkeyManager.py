from pynput import keyboard
import yaml

from dofus_window_manager.DofusWindowManager import DofusWindowManager
from global_hotkeys.GlobalHotkeysArguments import GlobalHotkeysArguments


class GlobalHotkeysManager:
    def __init__(self, yaml_config_path: str):
        with open(yaml_config_path, "r") as stream:
            try:
                self.configuration = GlobalHotkeysArguments()
                self.configuration.load_from_dict(yaml.safe_load(stream))
                print(f'self.configuration: {self.configuration.characters}')
            except yaml.YAMLError as exc:
                raise exc

        self.dofus_window_manager = DofusWindowManager(self.configuration.characters)

    def build_global_hotkey_dict(self):
        """
        Build the dictionary of global hotkeys using the initialized configuration.
        """
        hotkey_dict = {
            self.configuration.hotkeys.init_process_list: self.dofus_window_manager.init_dofus_window_handles,
            self.configuration.hotkeys.focus_next_character_window: self.dofus_window_manager.focus_next_character_window,
            self.configuration.hotkeys.focus_previous_character_window: self.dofus_window_manager.focus_previous_character_window,
        }

        # Bind the hotkeys for each character
        for i, character in enumerate(self.configuration.characters):
            if (i + 1) > 8:
                raise Exception(f'Cannot bind more than 8 characters to hotkeys. {character} is not bound.')
            hotkey_dict[getattr(self.configuration.hotkeys, f'focus_character_{i + 1}_window')] =\
                self.dofus_window_manager.focus_character_window_maker(character)

        return hotkey_dict

    def start(self):
        global_hotkey_dict = self.build_global_hotkey_dict()
        print(f'global_hotkey_dict: {global_hotkey_dict}')
        listener = keyboard.GlobalHotKeys(self.build_global_hotkey_dict())
        listener.start()
        listener.join()
