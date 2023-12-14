from abc import ABC, abstractmethod


class Menu(ABC):
    """An abstract base class defining the structure for various menu implementations."""

    @abstractmethod
    def run(self):
        """An abstract method that will be implemented by subclasses.
        This method defines the behavior of the menu when it is executed."""
        pass
