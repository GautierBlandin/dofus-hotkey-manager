from hotkey_managers.Suspender import Suspender


def test_suspender():
    def function_to_suspend():
        return 0

    suspender = Suspender()
    assert suspender.suspended is False
    assert suspender.make_suspendable(function_to_suspend)() == 0
    suspender.set_suspended(True)
    assert suspender.suspended is True
    assert suspender.make_suspendable(function_to_suspend)() is None
    suspender.set_suspended(False)
    assert suspender.suspended is False
    assert suspender.make_suspendable(function_to_suspend)() == 0
    suspender.toggle_suspended()
    assert suspender.suspended is True
    assert suspender.make_suspendable(function_to_suspend)() is None
    suspender.toggle_suspended()
    assert suspender.suspended is False
    assert suspender.make_suspendable(function_to_suspend)() == 0
