
from abc import ABC, abstractmethod


class Menu(ABC):

    @abstractmethod
    def run(self):
        pass
