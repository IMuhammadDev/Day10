# Calculator project
import art


# function add
def add(num1, num2):
    return num1 + num2


# function subtract
def subtract(num1, num2):
    return num1 - num2


# function multiply
def multiply(num1, num2):
    return num1 * num2


# function divide
def divide(num1, num2):
    return num1 / num2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculate():
    print(art.logo)
    first = float(input("What's the first number ?: "))
    for symbol in operations:
        print(symbol)
    condition = True
    while condition:
        operation = input("Pick an operation: ")
        second = float(input("What's the next number ?: "))
        calculation_function = operations[operation]
        first_result = calculation_function(first, second)
        print(f" {first} {operation} {second} = {first_result} ")
        if input(
                f"Type 'y' to continue calculating with {first_result}, or type 'n' to start a new calculation. (off "
                f"= '0' ): ") == "y":
            first = first_result
        else:
            condition = False
            calculate()


calculate()

"""
condition = True
while condition:
    first_num = int(input("What's the first number ?: "))
    operation = input("+\n-\n*\n/\nPick an operation: ")
    second_num = int(input("What's the next number ?: "))
    if operation == "+":
        result = add(first_num, second_num)
        print(f"{first_num} + {second_num} = {result}")
    elif operation == "-":
        result = subtract(first_num, second_num)
        print(f"{first_num} - {second_num} = {result}")
    elif operation == "*":
        result = multiply(first_num, second_num)
        print(f"{first_num} * {second_num} = {result}")
    elif operation == "/":
        result = divide(first_num, second_num)
        print(f"{first_num} / {second_num} = {result}")
    else:
        print("You choosed incorrect operation")
    ask = input(
        f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation. (off = '0' ): ")
    if ask == "n":
        result = 0
    elif ask == "o":
        condition = False
"""
