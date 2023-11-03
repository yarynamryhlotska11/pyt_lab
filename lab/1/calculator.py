import math


def add(number1, number2):
    if isinstance(number1, (int, float)) and isinstance(number2, (int, float)):
        return number1 + number2
    else:
        raise TypeError("Error! Both arguments must be numeric")


def subtract(number1, number2):
    if isinstance(number1, (int, float)) and isinstance(number2, (int, float)):
        return number1 - number2
    else:
        raise TypeError("Error! Both arguments must be numeric")


def multiply(number1, number2):
    if isinstance(number1, (int, float)) and isinstance(number2, (int, float)):
        return number1 * number2
    else:
        raise TypeError("Error! Both arguments must be numeric")


def divide(number1, number2):
    if isinstance(number1, (int, float)) and isinstance(number2, (int, float)):
        if number2 == 0:
            raise ZeroDivisionError("Error! Dividing by zero isn't possible")
        return number1 / number2
    else:
        raise TypeError("Error! Both arguments must be numeric")


def raise_num_to_power(number1, number2):
    if isinstance(number1, (int, float)) and isinstance(number2, (int, float)):
        return number1 ** number2
    else:
        raise TypeError("Error! Both arguments must be numeric")


def calculate_square_root(number):
    if isinstance(number, (int, float)):
        if number < 0:
            raise ArithmeticError("Error! The square root of a negative number cannot be calculated")
        return math.sqrt(number)
    else:
        raise TypeError("Error! Both arguments must be numeric")


def calculate_remainder_from_division(number1, number2):
    if isinstance(number1, (int, float)) and isinstance(number2, (int, float)):
        return number1 % number2
    elif number2 == 0:
        raise ZeroDivisionError("Impossible to divide")
    else:
        raise TypeError("Error! Both arguments must be numeric")


def change_decimal_places(value):
    global decimal_places
    if value <= 0:
        raise ArithmeticError("Error! Decimal digits must be greater than zero")
    decimal_places = value

