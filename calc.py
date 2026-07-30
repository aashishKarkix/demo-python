def calculate(num1, operator, num2):
    if operator == "+":
        return num1 + num2
    if operator == "-":
        return num1 - num2
    if operator == "*":
        return num1 * num2
    if operator == "/":
        if num2 == 0:
            raise ZeroDivisionError("Division by zero is not allowed.")
        return num1 / num2
    raise ValueError("Invalid operator.")


if __name__ == "__main__":
    # Simple Calculator
    num1 = float(input("Enter first number: "))
    operator = input("Enter operator (+, -, *, /): ")

    try:
        num2 = float(input("Enter second number: "))
        result = calculate(num1, operator, num2)
        print("Result:", result)
    except ZeroDivisionError as error:
        print("Error:", error)
    except ValueError as error:
        print(error)
