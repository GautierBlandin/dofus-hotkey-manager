from abc import ABC, abstractmethod
from typing import Union


class AbstractProcessManager(ABC):
    """
    Abstract class for process manager

    Interface:
    get_process_ids_by_name(process_name: str) -> list[int]
    get_window_handles_from_pid(pid: int) -> list[int]
    get_window_title_from_handle(hwnd: int) -> str
    get_window_handle_from_title(title: str, process_list: list[int]) -> Union[int, None]
    """

    @abstractmethod
    def get_process_ids_by_name(self, process_name: str) -> list[int]:
        pass

    @abstractmethod
    def get_window_handles_from_pid(self, pid: int) -> list[int]:
        pass

    @abstractmethod
    def get_window_title_from_handle(self, hwnd: int) -> str:
        pass

    @abstractmethod
    def get_window_handle_from_title(self, title: str, process_list: list[int]) -> Union[int, None]:
        pass

    @abstractmethod
    def set_foreground_window(self, hwnd: int) -> None:
        pass
