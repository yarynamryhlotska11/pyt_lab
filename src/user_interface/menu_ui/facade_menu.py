import os
from ui.menu.docs_menu import DocsMenu
from ui.menu.lab2.calculator_menu import CalculatorMenu
from ui.menu.lab3.ascii_art_generator_menu import AsciiArtGeneratorMenu
from ui.menu.lab5.figures import FigureMenu
from ui.menu.lab7.user_menu import UserMenu
from ui.menu.lab8.diagrams_menu import DiagramMenu
from shared.json_utility import read_json_file


class MenuFacade:

    def __init__(self):
        read_json_file("configuration/paths_config.json")
        json_data = read_json_file(file_path="../src/configuration/paths_config.json")
        self.__menus = [("Calculator", CalculatorMenu()),
                        ("AsciiArtGeneratorMenu", AsciiArtGeneratorMenu()),
                        ("FigureMenu", FigureMenu()),
                        ("UserMenu", UserMenu()),
                        ("DiagramMenu", DiagramMenu()),
                        ("DocsMenu", DocsMenu(os.path.abspath(json_data["HTML_DATA"])))]

        self.__finish_number = 0

    def print_menu_options(self):

        for index, (name, _) in enumerate(self.__menus, start=1):
            print(f"{index}. {name}")
        print(f"{self.__finish_number}. Exit")

    def start(self):

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
