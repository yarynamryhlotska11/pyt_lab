"""Module for implementing a calculator menu."""
from service.lab2.calculator_service import CalculatorService
from user_interface.menu_builder import Menu


class CalculatorMenu(Menu):
    """
    The 'CalculatorMenu' class offers a menu-driven interface for a calculator application. It utilizes functionalities
    from the 'CalculatorService' class to perform calculations based on user input.
    The 'CalculatorMenu' class inherits from the abstract base class 'Menu' and implements a user interface for a
    calculator system.
    """

    def run(self):
        """
        Run the calculator program.

        Initializes the 'CalculatorService' and runs the calculator menu in a loop until the user chooses to exit.
        """
        calculator_service = CalculatorService()

        while True:
            try:
                self.display_menu()
                choice = input("Enter your choice: ")

                if choice == '1':
                    calculator_service.input_values()
                    print(f"The result is {calculator_service.calculate()}")
                elif choice == '0':
                    break
                else:
                    print("Invalid choice. Please try again.")

            except ValueError as ve:
                print(f"Invalid input: {ve}")

    @staticmethod
    def display_menu():
        """Display the calculator menu."""
        print("1. Do calculation")
        print("0. Exit")
