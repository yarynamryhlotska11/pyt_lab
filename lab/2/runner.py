from calculator import *
from console_output import *


def main():
    calculator = Calculator()
    output = ConsoleOutput()

    while True:
        output.show_message("""
        Available operations:
        + : Sum of numbers
        - : Difference of numbers
        * : Product of numbers
        / : Division of numbers
        ^ : Exponentiation of a number
        % : Remainder from division
        √ : Calculation of the square root
        0 : Exit
        1 : View history
        2 : Open settings
        """)

        input_action = output.get_user_input("Enter the action you want to perform: ")

        if input_action == "0":
            break
        elif input_action in ("+", "-", "*", "/", "^", "%"):
            try:
                first_number = float(output.get_user_input("Enter the first number: "))
                second_number = float(output.get_user_input("Enter the second number: "))
                result = calculator.calculate(input_action, first_number, second_number)
                output.show_message(f"Result: {result}")
            except ValueError as e:
                output.show_message(str(e))
        elif input_action == "√":
            try:
                number = float(output.get_user_input("Enter a number: "))
                result = calculator.calculate(input_action, number, 0)
                output.show_message(f"Result: {result}")
            except ValueError as e:
                output.show_message(str(e))
        elif input_action == "1":
            history = calculator.view_history()
            output.show_message(history)
        elif input_action == "2":
            output.show_message(calculator.view_settings())
            inner_input_value = output.get_user_input("""Available options:
            0: Exit
            1: Change decimal places
            2: Clear history
            Your option is """)
            if inner_input_value == "0":
                pass
            elif inner_input_value == "1":
                try:
                    new_value = int(output.get_user_input("Enter a new value for decimal places: "))
                    calculator.change_decimal_places(new_value)
                    output.show_message(f"Decimal places set to {new_value}")
                except ValueError as e:
                    output.show_message(str(e))
            elif inner_input_value == "2":
                calculator.calculations_history.clear()
                output.show_message("History cleared")
            else:
                output.show_message("Invalid option")


if __name__ == "__main__":
    main()
