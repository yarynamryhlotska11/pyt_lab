import math


def add(number1, number2):
    return number1 + number2


def subtract(number1, number2):
    return number1 - number2


def multiply(number1, number2):
    return number1 * number2


def divide(number1, number2):
    if number2 == 0:
        raise ArithmeticError("Error! Dividing by zero isn't possible")
    return number1 / number2


def raise_num_to_power(number1, number2):
    return number1 ** number2


def calculate_square_root(number):
    if number < 0:
        raise ArithmeticError("Error! The square root of a negative number cannot be calculated")
    return math.sqrt(number)


def calculate_remainder_from_division(number1, number2):
    return number1 % number2


def change_decimal_places(value):
    global decimal_places
    if value <= 0:
        raise ArithmeticError("Error! Decimal digits must be greater than zero")
    decimal_places = value

