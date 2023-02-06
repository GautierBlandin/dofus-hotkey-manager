import yaml


class SmithmagicHotkeys:
    def __init__(self):
        self.toggle_smithmagic_hotkeys: str = ''
        self.rune_1: str = ''
        self.rune_2: str = ''
        self.rune_3: str = ''
        self.rune_4: str = ''
        self.rune_5: str = ''
        self.rune_6: str = ''
        self.rune_7: str = ''
        self.rune_8: str = ''
        self.rune_9: str = ''
        self.rune_10: str = ''
        self.rune_11: str = ''
        self.rune_12: str = ''
        self.rune_13: str = ''
        self.pa_modifier: str = ''
        self.ra_modifier: str = ''

    def load_from_dict(self, dict_to_load):
        for key, value in dict_to_load.items():
            setattr(self, key, value)


class SmithmagicScreenPositions:
    def __init__(self):
        self.normal_column_x_axis_position: int = 0
        self.pa_column_x_axis_position: int = 0
        self.ra_column_x_axis_position: int = 0
        self.rune_1_y_axis_position: int = 0
        self.rune_2_y_axis_position: int = 0
        self.rune_3_y_axis_position: int = 0
        self.rune_4_y_axis_position: int = 0
        self.rune_5_y_axis_position: int = 0
        self.rune_6_y_axis_position: int = 0
        self.rune_7_y_axis_position: int = 0
        self.rune_8_y_axis_position: int = 0
        self.rune_9_y_axis_position: int = 0
        self.rune_10_y_axis_position: int = 0
        self.rune_11_y_axis_position: int = 0
        self.rune_12_y_axis_position: int = 0
        self.rune_13_y_axis_position: int = 0

    def load_from_dict(self, dict_to_load):
        for key, value in dict_to_load.items():
            setattr(self, key, value)


class SmithmagicArguments:
    def __init__(self):
        self.hotkeys = SmithmagicHotkeys()
        self.rune_positions = SmithmagicScreenPositions()

    def load_from_dict(self, dict_to_load):
        for key, value in dict_to_load.items():
            if key == 'hotkeys':
                self.hotkeys.load_from_dict(value)
            if key == 'rune_positions':
                self.rune_positions.load_from_dict(value)

    def load_from_yaml(self, yaml_config_path: str):
        with open(yaml_config_path, "r") as stream:
            try:
                self.load_from_dict(yaml.safe_load(stream))
            except yaml.YAMLError as exc:
                print(exc)
