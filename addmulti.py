def add_and_multiply(a, b):
    return a + b, a * b


if __name__ == "__main__":
    print("Simple Calculator")

    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    sum_value, product_value = add_and_multiply(a, b)
    print("Sum =", sum_value)
    print("Product =", product_value)
