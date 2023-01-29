from typing import Union

import wmi
import ctypes
import win32process
import win32gui
import win32com.client

from process_manager.AbstractProcessManager import AbstractProcessManager

EnumWindows = ctypes.windll.user32.EnumWindows
EnumWindowsProc = ctypes.WINFUNCTYPE(ctypes.c_bool, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int))
GetWindowText = ctypes.windll.user32.GetWindowTextW
GetWindowTextLength = ctypes.windll.user32.GetWindowTextLengthW
IsWindowVisible = ctypes.windll.user32.IsWindowVisible


class ProcessManager(AbstractProcessManager):
    def set_foreground_window(self, hwnd: int) -> None:
        shell = win32com.client.Dispatch("WScript.Shell")
        shell.SendKeys('%')
        win32gui.SetForegroundWindow(hwnd)

    def get_process_ids_by_name(self, process_name: str) -> list[int]:
        pids = []
        process_name = process_name

        for proc in wmi.WMI().Win32_Process():
            if process_name == proc.Name:
                pids.append(proc.ProcessId)

        return pids

    def get_window_handles_from_pid(self, pid: int) -> list[int]:
        def callback(hwnd, hwnds):
            # if win32gui.IsWindowVisible(hwnd) and win32gui.IsWindowEnabled(hwnd):
            _, found_pid = win32process.GetWindowThreadProcessId(hwnd)

            if found_pid == pid:
                hwnds.append(hwnd)
            return True

        hwnds = []
        win32gui.EnumWindows(callback, hwnds)
        return hwnds

    def get_window_title_from_handle(self, hwnd: int) -> str:
        length = GetWindowTextLength(hwnd)
        buff = ctypes.create_unicode_buffer(length + 1)
        GetWindowText(hwnd, buff, length + 1)
        return buff.value

    def get_window_handle_from_title(self, title: str, process_list: list[int]) -> Union[int, None]:
        for pid in process_list:
            for hwnd in self.get_window_handles_from_pid(pid):
                if title in self.get_window_title_from_handle(hwnd):
                    return hwnd
        return None
