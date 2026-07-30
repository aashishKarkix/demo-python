def add_and_subtract(a, b):
    return a + b, a - b


if __name__ == "__main__":
    print("Simple Calculator")

    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    sum_value, diff_value = add_and_subtract(a, b)
    print("Sum =", sum_value)
    print("Difference =", diff_value)

