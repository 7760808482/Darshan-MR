def DivExp(a, b):
    assert a > 0, "The value of 'a' must be greater than 0"
    if b == 0:
        raise ZeroDivisionError("Division by zero is not allowed")
    return a / b

try:
    a = float(input("Enter a (> 0): "))
    b = float(input("Enter b: "))
    print("Result:", DivExp(a, b))
except AssertionError as e:
    print("Assertion Error:", e)
except ZeroDivisionError as e:
    print("Error:", e)
except ValueError:
    print("Invalid input. Enter numeric values.")