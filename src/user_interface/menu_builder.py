"""
Module Overview: Menu Management

This module introduces an abstract base class named 'Menu' and a 'MenuFacade' class dedicated to orchestrating a
collection of menus. The 'Menu' class acts as a prototype guiding the creation of individual menus, while the
'MenuFacade' class offers a simplified interface to interact with multiple menus.

Classes:
- Menu: An abstract base class defining the structure for various menu implementations.
- MenuFacade: A facilitator class responsible for coordinating and presenting a set of menus to users.

Usage:
Begin by creating instances of specialized menu classes that inherit from the 'Menu' class, tailoring them to specific
functionalities or tasks. Then, utilize the 'MenuFacade' class to manage these menus collectively, streamlining user
interactions and navigation through the menu system.
"""
from abc import ABC, abstractmethod


class Menu(ABC):
    """
    A description of the entire function, its parameters, and return types.
    """
    @abstractmethod
    def run(self):
        """
        An abstract method that will be implemented by subclasses. This method defines the behavior of the menu when it
        is executed.
        """
