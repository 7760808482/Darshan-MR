try:
    x = int("abc")
except ValueError:
    print("Invalid input")
finally:
    print("Program finished")


try:
    num=int(input("Enter the number:"))
    num1=num*num
    print(num1)
except ValueError:
    print("input is not a number")


try:
    a = 10
    b = 0
    print(a / b)
except ZeroDivisionError:
    print("Error: Division by zero")
finally:
    print("Program finished")



