def get_valid_number(prompt):
    while True:
        try:
            number = float(input(prompt))
            return number
        except ValueError:
            print("Invalid number. Please enter a valid float.")

def get_valid_operator():
    while True:
        operator = input("Enter your operator (+ - * / %): ")
        if operator in ["+", "-", "*", "/", "%"]:
            return operator
        else:
            print("Invalid operator. Please enter one of +, -, *, /, or %.")

Num1 = get_valid_number("Enter the 1st number: ")
Operator = get_valid_operator()
Num2 = get_valid_number("Enter the 2nd number: ")

try:
    if Operator == "+":
        Result = Num1 + Num2
    elif Operator == "-":
        Result = Num1 - Num2
    elif Operator == "*":
        Result = Num1 * Num2
    elif Operator == "/":
        Result = Num1 / Num2
    elif Operator == "%":
        Result = Num1 % Num2
    print(round(Result, 2))
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except Exception as e:
    print(f"An error occurred: {e}")

