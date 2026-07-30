def add_and_divide(a, b):
    return a + b, a / b


if __name__ == "__main__":
    print("Simple Calculator")

    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    sum_value, product_value = add_and_divide(a, b)
    print("Sum =", sum_value)
    print("divide =", product_value)
