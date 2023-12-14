"""
Module Overview: Menu Implementation

This module introduces an abstract base class named 'Menu' that provides the structure for various menu implementations.
The 'Menu' class is intended to be subclassed, offering a blueprint for creating specific menu functionalities.

Classes:
- Menu: An abstract base class defining the structure for different menu implementations.

Usage:
This module serves as a foundation for defining menu structures. Subclasses of 'Menu' should implement the abstract
'run' method to define the specific behavior of each menu when executed.
"""
from abc import ABC, abstractmethod


class Menu(ABC):
    """An abstract base class defining the structure for various menu implementations.

        Methods:
            run(self):
                An abstract method that needs to be implemented by subclasses.
                This method defines the behavior of the menu when it is executed.
        """
    @abstractmethod
    def run(self):
        """An abstract method that will be implemented by subclasses.
        This method defines the behavior of the menu when it is executed."""
        pass
