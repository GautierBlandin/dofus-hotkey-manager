from pynput import keyboard, mouse
import yaml
import threading

from dofus_window_manager.DofusWindowManager import DofusWindowManager
from hotkey_managers.multi_account_manager.MultiAccountArguments import GlobalHotkeysArguments
from hotkey_managers.Suspender import Suspender
from mouse_automation.mouse.Mouse import IMouse
from mouse_automation.MouseRepeater import MouseRepeater
from mouse_automation.MouseCoordPrinter import MouseCoordPrinter
from hotkey_managers.AbstrasctManager import AbstractManager
import hotkey.GlobalHotkeyListener


class MultiAccountHotkeysManager(AbstractManager):
    def __init__(self, yaml_config_path: str, abstract_mouse: IMouse):
        with open(yaml_config_path, "r") as stream:
            try:
                self.configuration = GlobalHotkeysArguments()
                self.configuration.load_from_dict(yaml.safe_load(stream))
                print(f'Registered characters: {self.configuration.characters}')
                print(f'Registered hotkeys: {self.configuration.hotkeys.__dict__}')
            except yaml.YAMLError as exc:
                raise exc

        self.dofus_window_manager = DofusWindowManager(self.configuration.characters)
        self.mouse_repeater = MouseRepeater(self.dofus_window_manager, abstract_mouse)
        self.mouse_coord_printer = MouseCoordPrinter(abstract_mouse)
        self.suspender = Suspender(True)

    def build_global_hotkey_dict(self):
        """
        Build the dictionary of global hotkeys using the initialized configuration.
        """
        hotkey_dict = {
            self.configuration.hotkeys.suspend: self.suspender.toggle_suspended,
            self.configuration.hotkeys.init_process_list: self.suspender.make_suspendable(self.dofus_window_manager.init_dofus_window_handles),
            self.configuration.hotkeys.focus_next_character_window: self.suspender.make_suspendable(self.dofus_window_manager.focus_next_character_window),
            self.configuration.hotkeys.focus_previous_character_window: self.suspender.make_suspendable(self.dofus_window_manager.focus_previous_character_window),
            self.configuration.hotkeys.toggle_click_repetition: self.suspender.make_suspendable(self.mouse_repeater.toggle_active),
            self.configuration.hotkeys.toggle_mouse_coord_printing: self.suspender.make_suspendable(self.mouse_coord_printer.toggle_active)
        }

        # Bind the hotkeys for each character
        for i, character in enumerate(self.configuration.characters):
            if (i + 1) > 8:
                raise Exception(f'Cannot bind more than 8 characters to hotkeys. {character} is not bound.')
            hotkey_dict[getattr(self.configuration.hotkeys, f'focus_character_{i + 1}_window')] =\
                self.suspender.make_suspendable(self.dofus_window_manager.focus_character_window_maker(character))

        return hotkey_dict

    def get_listeners(self) -> list[threading.Thread]:
        global_hotkey_dict = self.build_global_hotkey_dict()
        keyboard_listener = hotkey.GlobalHotkeyListener.GlobalHotkeyListener(global_hotkey_dict)

        mouse_repeater_listener = mouse.Listener(
            on_click=self.mouse_repeater.on_click,
        )

        mouse_printer_listener = mouse.Listener(
            on_click=self.mouse_coord_printer.on_click,
        )

        return [mouse_repeater_listener, keyboard_listener, mouse_printer_listener]
