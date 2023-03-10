from hotkey_managers.smithmagic_manager.SmithmagicArguments import SmithmagicArguments
import os

def test_smithmagic_arguments():
    """Test smithmagic_manager arguments."""
    script_dir = os.path.dirname(__file__)
    rel_path = './smithmagic_test_configuration.yaml'
    abs_file_path = os.path.join(script_dir, rel_path)

    smithmagic_arguments = SmithmagicArguments()
    smithmagic_arguments.load_from_yaml(abs_file_path)
    assert smithmagic_arguments.rune_positions.normal_column_x_axis_position == 1000
    assert smithmagic_arguments.rune_positions.rune_1_y_axis_position == 100
    assert smithmagic_arguments.rune_positions.rune_13_y_axis_position == 100
    assert smithmagic_arguments.hotkeys.toggle_smithmagic_hotkeys == '<alt>+<ctrl>+m'
    assert smithmagic_arguments.hotkeys.rune_1 == 'q'
    assert smithmagic_arguments.hotkeys.rune_13 == 'h'
    assert smithmagic_arguments.hotkeys.ra_modifier == '<ctrl>'
