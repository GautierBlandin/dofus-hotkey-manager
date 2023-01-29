from dofus_window_manager.AbstractDofusWindowManager import AbstractDofusWindowManager


class StubDofusWindowManager(AbstractDofusWindowManager):
    """
    Stub class for dofus window manager
    """

    def __init__(self, character_names: list[str]):
        self.initialized = False
        self.dofus_window_handles = None
        self.character_names = character_names

    def init_dofus_window_handles(self) -> None:
        self.initialized = True
        for character_name in self.character_names:
            self.dofus_window_handles[character_name] = 0

    def focus_character_window(self, character_name) -> None:
        if not self.initialized:
            raise Exception("StubDofusWindowManager not initialized")
        if character_name not in self.dofus_window_handles:
            raise Exception("Character not found")
        print("StubDofusWindowManager.focus_character_window: " + character_name)

    def focus_next_character_window(self) -> None:
        if not self.initialized:
            raise Exception("StubDofusWindowManager not initialized")
        print("StubDofusWindowManager.focus_next_character_window")

    def focus_previous_character_window(self) -> None:
        if not self.initialized:
            raise Exception("StubDofusWindowManager not initialized")
        print("StubDofusWindowManager.focus_previous_character_window")
