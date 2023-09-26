# Task 1,2
while True:
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        operator = input("Enter operator (+, -, *, /): ")

        if operator in ('+', '-', '*', '/'):
            break  # Exit the loop if the operator is valid
        else:
            print("Error! The operator entered is not valid. Please enter one of +, -, *, /.")
    except ValueError:
        print("Error! Enter the correct number.")

if operator == '+':
    result = num1 + num2
    print(f"The result of the addition: {num1} + {num2} = {result}")
elif operator == '-':
    result = num1 - num2
    print(f"The result of the subtraction: {num1} - {num2} = {result}")
elif operator == '*':
    result = num1 * num2
    print(f"The result of multiplication: {num1} * {num2} = {result}")
elif operator == '/':
    if num2 != 0:
        result = num1 / num2
        print(f"The result of division: {num1} / {num2} = {result}")
    else:
        print("Error! Division by zero is impossible.")
