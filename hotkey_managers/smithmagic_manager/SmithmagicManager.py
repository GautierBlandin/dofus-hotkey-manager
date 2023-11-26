from typing import Callable, Protocol
from abc import abstractmethod
import threading
from pynput import keyboard

import hotkey.GlobalHotkeyListener
from hotkey_managers.Suspender import Suspender
from hotkey_managers.smithmagic_manager.SmithmagicArguments import SmithmagicArguments
from decorators.common import make_caller
from hotkey_managers.AbstrasctManager import AbstractManager


class IMouse(Protocol):
    @abstractmethod
    def click(self, x, y):
        raise NotImplementedError


class SmithmagicManager(AbstractManager):
    def __init__(self, smithmagic_arguments: SmithmagicArguments, mouse: IMouse):
        self.configuration = smithmagic_arguments
        self.suspender = Suspender(suspended=True)
        self.mouse = mouse

    @staticmethod
    def create_from_yaml(yaml_configuration_path: str, mouse: IMouse):
        return SmithmagicManager(SmithmagicArguments().load_from_yaml(yaml_configuration_path), mouse)

    def _build_hotkey_string(self, sub_hotkeys_string: list[str]):
        return '+'.join(sub_hotkeys_string)

    def create_hotkey_dictionary(self):
        hotkey_dict: dict[str, Callable[[], None]] = {
            self.configuration.hotkeys.toggle_smithmagic_hotkeys: self.suspender.toggle_suspended,
            self.configuration.hotkeys.fusion: self.suspender.make_suspendable(make_caller(
                self.mouse.click,
                x=self.configuration.rune_positions.fusion_x_position,
                y=self.configuration.rune_positions.fusion_y_position
            )),
            self.configuration.hotkeys.fusion_all: self.suspender.make_suspendable(make_caller(
                self.mouse.click,
                x=self.configuration.rune_positions.fusion_all_x_position,
                y=self.configuration.rune_positions.fusion_all_y_position
            ))
        }

        for i in range(1, 14):
            row_position_property_name = f'rune_{i}_y_axis_position'
            rune_hotkey_property_name = f'rune_{i}'
            column_position_property_name = 'normal_column_x_axis_position'
            hotkey_dict[self.configuration.hotkeys.__getattribute__(rune_hotkey_property_name)] = self.suspender.make_suspendable(
                make_caller(
                    self.mouse.click,
                    x=self.configuration.rune_positions.__getattribute__(column_position_property_name),
                    y=self.configuration.rune_positions.__getattribute__(row_position_property_name)
                ))

            column_position_property_name = 'pa_column_x_axis_position'
            hotkey = self._build_hotkey_string([self.configuration.hotkeys.pa_modifier,
                                                self.configuration.hotkeys.__getattribute__(rune_hotkey_property_name)])
            hotkey_dict[hotkey] = self.suspender.make_suspendable(
                make_caller(
                    self.mouse.click,
                    x=self.configuration.rune_positions.__getattribute__(column_position_property_name),
                    y=self.configuration.rune_positions.__getattribute__(row_position_property_name)
                ))

            column_position_property_name = 'ra_column_x_axis_position'
            hotkey = self._build_hotkey_string([self.configuration.hotkeys.ra_modifier,
                                                self.configuration.hotkeys.__getattribute__(rune_hotkey_property_name)])
            hotkey_dict[hotkey] = self.suspender.make_suspendable(
                make_caller(
                    self.mouse.click,
                    x=self.configuration.rune_positions.__getattribute__(column_position_property_name),
                    y=self.configuration.rune_positions.__getattribute__(row_position_property_name)
                ))
        return hotkey_dict

    def get_listeners(self) -> list[threading.Thread]:
        hotkey_dict = self.create_hotkey_dictionary()
        keyboard_listener = hotkey.GlobalHotkeyListener.GlobalHotkeyListener(hotkey_dict)

        return [keyboard_listener]
