"""
The `math` module provides mathematical functions for performing mathematical operations in Python.

The `CalculatorService` class enables basic arithmetic calculations by inputting two values and an operator.
It supports operations such as addition, subtraction, multiplication, division, exponentiation, square root, and modulus.

Methods:
- __init__(self): Initializes the CalculatorService object with first_value, operator, and second_value set to None.
- input_values(self): Allows the user to input values for first_value, operator, and second_value, validating the input
and handling potential errors.
- __operator_is_correct(operator): Validates if the operator provided is correct and supported for arithmetic calculations.
- calculate(self): Performs the arithmetic calculation based on the provided operator and values, handling specific
cases like division by zero or calculating the square root of a negative number.
- __str__(self): Returns a formatted string containing the current state of the CalculatorService object.

Example:
from math import sqrt

calculator = CalculatorService()
calculator.input_values()
result = calculator.calculate()
print("Result:", result)

# Output: Enter first value: 9
#         Enter operator ['+', '-', '*', '/', '**', '√', '%']: √
#         Result: 3.0
"""

import math


class CalculatorService:

    def __init__(self):
        self.__first_value = None
        self.__operator = None
        self.__second_value = None

    def input_values(self):
        try:
            self.__first_value = float(input("Enter first value: "))
            self.__operator = str(input("Enter operator ['+', '-', '*', '/', '**', '√', '%']: "))
            if self.__operator_is_correct(self.__operator):
                if self.__operator != "√":
                    self.__second_value = float(input("Enter second value: "))
            else:
                raise RuntimeWarning("Error! You input incorrect operator")
        except ValueError as e:
            raise type(e)("Format of the number is invalid")

    @staticmethod
    def __operator_is_correct(operator):
        valid_operators = ('+', '-', '*', '/', '**', '√', '%')
        return operator in valid_operators

    def calculate(self):
        result = 0  # Initialize result to handle the "%"

        if self.__operator == "+":
            result = self.__first_value + self.__second_value
        elif self.__operator == "-":
            result = self.__first_value - self.__second_value
        elif self.__operator == "*":
            result = self.__first_value * self.__second_value
        elif self.__operator == "/":
            if self.__second_value == 0:
                raise ZeroDivisionError("Error! Impossible divide to 0 ")
            result = self.__first_value / self.__second_value
        elif self.__operator == "**":
            result = self.__first_value ** self.__second_value
        elif self.__operator == "√":
            if self.__first_value < 0:
                raise ArithmeticError("Error! It is impossible to calculate the square root from negative number")
            result = math.sqrt(self.__first_value)
        elif self.__operator == "%":
            result = self.__first_value % self.__second_value

        return result

    def __str__(self):
        return f"CalculatorService: first_value={self.__first_value}, operator={self.__operator}," \
               f"second_value={self.__second_value}"

