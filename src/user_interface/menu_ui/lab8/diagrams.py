"""
Menu Diagrams Module

This module defines the `DiagramMenu` class, representing a
 menu for displaying diagrams.

Note: Ensure the required libraries (`sys`) are
installed before using this module.
"""
from service.lab8.diagrams_service import DiagramServiceImpl
from shared.json_utility import read_json_file
from user_interface.menu_builder import Menu


class DiagramMenu(Menu):
    """Menu class for managing diagram creation and display.

    This class presents a menu system to create and display different types of diagrams
    using the DiagramServiceImpl. Users can select options to display state histograms,
    pie charts, or complicated diagrams.

    Attributes:None

    Methods:
        run(): Runs the menu system for diagram creation and display.
        display_diagram(diagram_function): Displays the chosen diagram based on the provided function.
    """

    def run(self):
        """Run the menu system for managing diagram creation and display."""
        json_data = read_json_file(file_path="../src/configuration/paths_config.json")
        service = DiagramServiceImpl(json_data["USERS_DATA"])

        while True:
            print(
                "1. Display state histogram\n"
                "2. Display pie chart\n"
                "3. Display complicated diagram\n"
                "0. Exit\n"
            )

            choice = input("Enter your choice: ")
            if choice == "1":
                self.display_diagram(service.create_states_histogram)
            elif choice == "2":
                self.display_diagram(service.create_pie_chart)
            elif choice == "3":
                self.display_diagram(service.create_combined_diagram)
            elif choice == "0":
                break
            else:
                print("Invalid choice. Enter again!")

    @staticmethod
    def display_diagram(diagram_function):
        """Display the chosen diagram based on the provided function."""
        has_to_be_downloaded = input(
            "Do you want to download the diagram? Enter 'y' or "
            "anything else not to download: ") == "y"

        diagram_function(has_to_be_downloaded)
