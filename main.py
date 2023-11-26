from hotkey_managers.multi_account_manager.MultiAccountManager import MultiAccountHotkeysManager
from hotkey_managers.smithmagic_manager.SmithmagicManager import SmithmagicManager
from mouse_automation.mouse.Mouse import Mouse
from keyboard_automation.Keyboard import Keyboard

mouse = Mouse()
keyboard = Keyboard()

mam_threads = MultiAccountHotkeysManager('multi_account_configuration.yaml', mouse, keyboard).get_listeners()
# smithmagic_threads = SmithmagicManager.create_from_yaml('smithmagic_configuration.yaml', mouse).get_listeners()

threads = mam_threads

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()
