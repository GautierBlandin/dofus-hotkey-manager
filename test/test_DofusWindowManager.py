from dofus_window_manager.DofusWindowManager import DofusWindowManager
from process_manager.StubProcessManager import StubProcessManager


def test_DofusWindowManager(capfd):
    stub_process_manager = StubProcessManager()
    dofus_window_manager = DofusWindowManager(['Character1', 'Character2', 'Character3', 'Character4'], stub_process_manager)
    dofus_window_manager.init_dofus_window_handles()
    out, err = capfd.readouterr()

    assert dofus_window_manager.dofus_window_handles['Character1'] == 12
    assert dofus_window_manager.dofus_window_handles['Character2'] == 22
    assert dofus_window_manager.dofus_window_handles['Character3'] == 32
    assert dofus_window_manager.dofus_window_handles['Character4'] == 42

    dofus_window_manager.focus_character_window('Character2')
    out, err = capfd.readouterr()
    assert out == 'Focused window 22\n'
    dofus_window_manager.focus_character_window('Character1')
    out, err = capfd.readouterr()
    assert out == 'Focused window 12\n'
    dofus_window_manager.focus_character_window('Character3')
    out, err = capfd.readouterr()
    assert out == 'Focused window 32\n'
    dofus_window_manager.focus_character_window('Character4')
    out, err = capfd.readouterr()
    assert out == 'Focused window 42\n'

    dofus_window_manager.focus_next_character_window()
    out, err = capfd.readouterr()
    assert out == 'Focused window 12\n'

    dofus_window_manager.focus_previous_character_window()
    out, err = capfd.readouterr()
    assert out == 'Focused window 42\n'

    dofus_window_manager.focus_previous_character_window()
    out, err = capfd.readouterr()
    assert out == 'Focused window 32\n'

    dofus_window_manager.focus_next_character_window()
    out, err = capfd.readouterr()
    assert out == 'Focused window 42\n'
