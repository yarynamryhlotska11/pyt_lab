"""
The module provides a text-based interactive menu for navigating through HTML documentation.
"""
import os
from user_interface.menu_ui.docs_ui_menu import DocsMenu
from user_interface.menu_ui.lab2.calculator import CalculatorMenu
from user_interface.menu_ui.lab3.ascii_generator import AsciiArtGeneratorMenu
from user_interface.menu_ui.lab5.figures_generator import FigureMenu
from user_interface.menu_ui.lab7.user import UserMenu
from user_interface.menu_ui.lab8.diagrams import DiagramMenu
from shared.json_utility import read_json_file


class MenuFacade:
    """Facade class for managing different menus in the application.

    The MenuFacade class acts as a central hub for accessing and navigating through various menus
    available in the application. It offers options to access different functionalities via specific
    menu choices.

    Attributes: None

    Methods:
        print_menu_options(): Prints the available menu options for user selection.
        start(): Begins the menu interaction process by prompting user input for menu choices.
    """

    def __init__(self):
        """Initialize the MenuFacade object."""
        read_json_file("configuration/paths_config.json")
        json_data = read_json_file(file_path="../src/configuration/paths_config.json")
        self.__menus = [
            ("Calculator", CalculatorMenu()),
            ("AsciiArtGeneratorMenu", AsciiArtGeneratorMenu()),
            ("FigureMenu", FigureMenu()),
            ("UserMenu", UserMenu()),
            ("DiagramMenu", DiagramMenu()),
            ("DocsMenu", DocsMenu(os.path.abspath(json_data["HTML_DATA"]))),
        ]

        self.__finish_number = 0

    def print_menu_options(self):
        """Print the available menu options for user selection."""

        for index, (name, _) in enumerate(self.__menus, start=1):
            print(f"{index}. {name}")
        print(f"{self.__finish_number}. Exit")

    def start(self):
        """Start the menu interaction process."""

        while True:
            self.print_menu_options()
            choice = input("Enter your choice: ")
            try:
                choice = int(choice)
                if choice == self.__finish_number:
                    break
                if not 1 <= choice <= len(self.__menus):
                    raise ValueError
                _, menu = self.__menus[choice - 1]
                menu.run()
            except ValueError:
                print("Invalid choice. Enter again!")
