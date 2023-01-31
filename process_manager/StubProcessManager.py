from typing import Union

from process_manager.AbstractProcessManager import AbstractProcessManager


class StubProcessManager(AbstractProcessManager):
    def get_process_ids_by_name(self, process_name: str) -> list[int]:
        if process_name == "Dofus.exe":
            return [1, 2, 3, 4]
        else:
            return []

    def get_window_handles_from_pid(self, pid: int) -> list[int]:
        return [10 * pid, 10 * pid + 1, 10 * pid + 2, 10 * pid + 3]

    def get_window_title_from_handle(self, hwnd: int) -> str:
        if hwnd % 10 == 2:
            return f'Character{hwnd // 10}'
        else:
            return f'Window{hwnd}'

    def get_window_handle_from_title(self, title: str, process_list: list[int]) -> Union[int, None]:
        for pid in process_list:
            for hwnd in self.get_window_handles_from_pid(pid):
                if title in self.get_window_title_from_handle(hwnd):
                    return hwnd
        return None

    def set_foreground_window(self, hwnd: int) -> None:
        print(f'Focused window {hwnd}')
