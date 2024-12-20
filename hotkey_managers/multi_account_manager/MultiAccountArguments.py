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
        self.focus_next_character_window: str = 'v'
        self.focus_previous_character_window: str = '<shift>+c'
        self.toggle_click_repetition: str = '<ctrl>+<alt>+r'
        self.toggle_mouse_coord_printing: str = '<ctrl>+<alt>+m'
        self.travel: str = '<ctrl>+<alt>+d'
        self.suspend: str = '<ctrl>+<alt>+s'

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
