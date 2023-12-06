import math


class Calculator:
    def __init__(self):
        self.calculations_history = []  # List to store calculation history
        self.decimal_places = 2  # Default decimal places

    def view_history(self):
        if not self.calculations_history:
            return "The history is empty"
        else:
            history = "Calculation history:\n"
            for item in self.calculations_history:
                history += " ".join(map(str, item)) + "\n"
            return history

    def view_settings(self):
        return f"Settings:\nDecimal places are {self.decimal_places}"

    def change_decimal_places(self, value):
        try:
            if value <= 0:
                raise ValueError("Error! Decimal places must be greater than zero")
            self.decimal_places = value
        except ValueError as e:
            return str(e)

    def calculate(self, operator, num1, num2):
        try:
            if operator == "+":
                result = num1 + num2
            elif operator == "-":
                result = num1 - num2
            elif operator == "*":
                result = num1 * num2
            elif operator == "/":
                if num2 == 0:
                    raise ValueError("Error! Division by zero is not allowed")
                result = num1 / num2
            elif operator == "^":
                result = num1 ** num2
            elif operator == "%":
                result = num1 % num2
            elif operator == "√":
                if num1 < 0:
                    raise ValueError("Error! Square root of a negative number is not allowed")
                result = math.sqrt(num1)
            else:
                raise ValueError("Error! Invalid operator")

            calculation = (num1, operator, num2, "=", round(result, self.decimal_places))
            self.calculations_history.append(calculation)
            return calculation[-1]
        except (ValueError, ZeroDivisionError) as e:
            return str(e)
