class Calculator:
    def __init__(self):
        self.result = None

    def get_user_input(self):
        try:
            number1 = float(input("Enter the first number: "))
            operator = input("Enter the operator (+, -, *, /): ")
            number2 = float(input("Enter the second number: "))
            return number1, operator, number2
        except ValueError:
            print("Invalid number format. Please try again.")
            return self.get_user_input()

    def check_operator(self, operator):
        valid_operators = ["+", "-", "*", "/"]
        if operator not in valid_operators:
            print("Unknown operator. Enter one of +, -, *, /")
            return False
        return True

    def calculate(self, number1, operator, number2):
        if not self.check_operator(operator):
            return

        try:
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
        except ZeroDivisionError:
            print("Error: Division by zero.")

    def display_result(self):
        if self.result is not None:
            print("Result: ", self.result)
        else:
            print("The result has not yet been calculated.")

    def run(self):
        while True:
            number1, operator, number2 = self.get_user_input()
            self.calculate(number1, operator, number2)
            self.display_result()

            another_calculation = input("Do you want to perform another calculation? (Yes/No): ").lower()
            if another_calculation != "yes":
                break


# Приклад використання класу Calculator
if __name__ == "__main__":
    calc = Calculator()
    calc.run()
