"""
Module: interactive_docs_ui_menu

This module provides a text-based interactive menu for navigating through HTML documentation.

Classes:
    - DocsMenu: Provides a text-based interactive menu for navigating through HTML documentation.
"""
from service.docs_service import DocsService


class DocsMenu:
    """Menu class for navigating through documentation pages.

    The DocsMenu class provides a menu interface to interact with documentation pages
    managed by the DocsService. It allows users to display, change, and navigate through
    pages within the documentation.

    Attributes:
        docs_service (DocsService): An instance of DocsService used for managing documentation.

    Methods:
        print_menu(): Displays the menu options for interacting with the documentation pages.
        run(): Initiates the menu interaction process for navigating through documentation pages.
    """

    def __init__(self, folder_path: str):
        """Initialize the DocsMenu object."""
        self.docs_service = DocsService(folder_path)

    @staticmethod
    def print_menu():
        """Display the menu options for interacting with documentation pages."""
        print("1. Display current page")
        print("2. Change to a specific page")
        print("3. Move to the next page")
        print("4. Move to the previous page")
        print("0. Exit")

    def run(self):
        """
        Initiate the menu interaction process for navigating documentation pages.
        This method runs a loop allowing users to select various options to navigate through the documentation pages.
        """
        while True:
            print("Current Page:", self.docs_service.current_page)
            self.print_menu()

            try:
                choice = int(input("Enter your choice: "))

                if choice == 1:
                    self.docs_service.display_page()
                elif choice == 2:
                    page_number = int(input("Enter the page number: "))
                    self.docs_service.change_page(page_number)
                elif choice == 3:
                    self.docs_service.next_page()
                elif choice == 4:
                    self.docs_service.prev_page()
                elif choice == 0:
                    break
                else:
                    print("Invalid choice. Please enter a corresponding number")
            except ValueError:
                print("Invalid input. Please enter a number.")
