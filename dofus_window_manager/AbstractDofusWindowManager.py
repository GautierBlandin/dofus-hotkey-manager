from abc import ABC, abstractmethod


class AbstractDofusWindowManager(ABC):
    """
    Abstract class for dofus window manager

    Interface:
    init_dofus_window_handles(character_names: list[str]) -> int
    focus_character_window(character_name) -> None
    focus_next_character_window() -> None
    focus_previous_character_window() -> None
    """

    @abstractmethod
    def init_dofus_window_handles(self) -> None:
        pass

    @abstractmethod
    def focus_character_window(self, character_name) -> None:
        pass

    @abstractmethod
    def focus_next_character_window(self) -> None:
        pass

    @abstractmethod
    def focus_previous_character_window(self) -> None:
        pass
