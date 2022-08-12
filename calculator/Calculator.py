logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

def add(n1, n2):
    return n1 + n2

def subtract (n1, n2):
    return n1 - n2

def divide (n1, n2):
    return n1 / n2

def multiply (n1, n2):
    return n1 * n2

operations = {
    "+": add, 
    "-": subtract, 
    "/": divide,
    "*": multiply
}

print (logo) 

def calculator():
    num1 = float(input("What's the first number?: "))

    for symbol in operations:
        print(symbol)

    more_operations = True 

    while more_operations:
        operation_symbol = input ("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        calculation_function = operations [operation_symbol]
        answer = calculation_function (num1, num2)

        print (f"{num1} {operation_symbol} {num2} = {answer}")

        continue_counting = input (f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation.: ")
        if continue_counting == "y":
            num1 = answer
        else:
            more_operations = False
            calculator()

calculator()