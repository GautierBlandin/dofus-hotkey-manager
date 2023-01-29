from typing import TypedDict

import yaml


class HotkeysDefinition:
    """
    Definition of hotkeys
    """
    def __init__(self):
        self.init_process_list: str = '<ctrl>+<alt>+i'
        self.focus_character_1_window: str = '<ctrl>+<alt>+1'
        self.focus_character_2_window: str = '<ctrl>+<alt>+2'
        self.focus_character_3_window: str = '<ctrl>+<alt>+3'
        self.focus_character_4_window: str = '<ctrl>+<alt>+4'
        self.focus_character_5_window: str = '<ctrl>+<alt>+5'
        self.focus_character_6_window: str = '<ctrl>+<alt>+6'
        self.focus_character_7_window: str = '<ctrl>+<alt>+7'
        self.focus_character_8_window: str = '<ctrl>+<alt>+8'
        self.focus_next_character_window: str = '<ctrl>+<alt>+n'
        self.focus_previous_character_window: str = '<ctrl>+<alt>+p'

    def load_from_dict(self, dict_to_load):
        for key, value in dict_to_load.items():
            setattr(self, key, value)


class GlobalHotkeysArguments:
    """
    Arguments for global hotkeys
    """
    def __init__(self):
        self.hotkeys = HotkeysDefinition()
        self.characters: list[str] = []

    def load_from_dict(self, dict_to_load):
        for key, value in dict_to_load.items():
            if key == 'hotkeys':
                self.hotkeys.load_from_dict(value)
            elif key == 'characters':
                self.characters = value

    def load_from_yaml(self, yaml_config_path: str):
        with open(yaml_config_path, "r") as stream:
            try:
                self.load_from_dict(yaml.safe_load(stream))
            except yaml.YAMLError as exc:
                print(exc)
