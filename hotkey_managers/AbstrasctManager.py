from abc import ABC, abstractmethod
import threading


class AbstractManager(ABC):
    @abstractmethod
    def get_listeners(self) -> list[threading.Thread]:
        raise NotImplementedError
