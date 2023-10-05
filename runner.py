from calculator import *
from console_output import *

calculations_history = []
decimal_places = 2

while True:
    print("Sum of numbers (+)")
    print("Difference of numbers (-)")
    print("Product of numbers (*)")
    print("Division of numbers (/)")
    print("Exponentiation of a number (^)")
    print("Remainder from division (%)")
    print("Calculation of the square root (√)")
    print("Exit (0)")
    print("View history (1)")
    print("Open settings (2)")

    input_action = input("The action you want to do is ")

    if input_action in ("+", "-", "*", "/", "^", "%"):
        first_number = float(input("Enter first number: "))
        second_number = float(input("Enter second number: "))

        try:
            match input_action:
                case "+":
                    action = "+"
                    result = add(first_number, second_number)
                case "-":
                    action = "-"
                    result = subtract(first_number, second_number)
                case "*":
                    action = "*"
                    result = multiply(first_number, second_number)
                case "/":
                    action = "/"
                    result = divide(first_number, second_number)
                case "^":
                    action = "^"
                    result = raise_num_to_power(first_number, second_number)
                case "%":
                    action = "%"
                    result = calculate_remainder_from_division(first_number, second_number)

            calculations_history += [(first_number, action, second_number, "=", result)]
            print("Result: " + str(round(result, decimal_places)) + "\n")
        except ArithmeticError as e:
            print(str(e) + "\n")
    elif input_action == "√":
        try:
            number = float(input("Enter number: "))
            result = calculate_square_root(number)

            calculations_history += [("√", number, "=", result)]
            print("Result: " + str(round(result, decimal_places)) + "\n")
        except ArithmeticError as e:
            print(str(e) + "\n")
    elif input_action == "1":
        view_history(calculations_history, decimal_places)
        print()
    elif input_action == "2":
        while True:
            print("\tSettings options:")
            print("\t0. Exit")
            print("\t1. View settings")
            print("\t2. Change decimal places")
            print("\t3. Clear the history of calculations")

            inner_input_value = str(input("\tYour option is "))

            if inner_input_value == "1":
                view_settings(decimal_places)
                print()
            elif inner_input_value == "2":
                new_value = int(input("\tEnter a new value for decimal places: "))
                try:
                    change_decimal_places(new_value)
                    print()
                except ArithmeticError as e:
                    print("\t" + str(e) + "\n")
            elif inner_input_value == "3":
                calculations_history.clear()
                print()
            elif inner_input_value == "0":
                print()
                break
            else:
                print("\tYou entered an incorrect option\n")
    elif input_action == "0":
        break
    else:
        print("You entered an incorrect action\n")
