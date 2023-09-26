#Task5
while True:
    try:
        num1 = float(input("Enter first number: "))
    except ValueError:
        print("Error! Enter a valid number for the first input.")
        continue  # Ask  again for the first number

    try:
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Error! Enter a valid number for the second input.")
        continue   # Ask  again for the second number

    while True:
        operator = input("Enter operator (+, -, *, /): ")
        if operator in ('+', '-', '*', '/'):
            break  # Exit if the operator is correct
        else:
            print("Error! The operator entered is not valid. Please enter one of +, -, *, /.")

    if operator == '/' and num2 == 0:
        print("Error! Division by zero is not allowed.")
    else:
        if operator == '+':
            result = num1 + num2
            print(f"The result of addition: {num1} + {num2} = {result}")
        elif operator == '-':
            result = num1 - num2
            print(f"The result of subtraction: {num1} - {num2} = {result}")
        elif operator == '*':
            result = num1 * num2
            print(f"The result of multiplication: {num1} * {num2} = {result}")
        elif operator == '/':
            result = num1 / num2
            print(f"The result of division: {num1} / {num2} = {result}")

    repeat = input("Continue to calculate? (Yes/No): ")
    if repeat.lower() != 'yes':
        break  # Exit if user don't want to continue