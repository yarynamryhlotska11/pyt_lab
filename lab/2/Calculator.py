class Calculator:
    def __init__(self):
        self.result = None

    def get_user_input(self):
        try:
            number1 = float(input("Enter the first number: "))
            operator = input("Enter the operator (+, -, *, /): ")
            number2 = float(input("Enter the second numberо: "))
            return number1, operator, number2
        except ValueError:
            print("Invalid number format. Please try again.")
            return self.get_user_input()

    def calculate(self, number1, operator, number2):
        if operator == "+":
            self.result = number1 + number2
        elif operator == "-":
            self.result = number1 - number2
        elif operator == "*":
            self.result = number1 * number2
        elif operator == "/":
            if number2 == 0:
                print("Division by zero is impossible.")
            else:
                self.result = number1 / number2
        else:
            print("Unknown operator.")

    def display_result(self):
        if self.result is not None:
            print("Result: ", self.result)
        else:
            print("The result has not yet been calculated.")


# Приклад використання класу Calculator
if __name__ == "__main__":
    calc = Calculator()
    number1, operator, number2 = calc.get_user_input()
    calc.calculate(number1, operator, number2)
    calc.display_result()
