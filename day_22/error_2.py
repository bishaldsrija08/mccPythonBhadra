try:
    num = int(input("Enter an integer: "))
    print(10/num)
except ValueError:
    print("Number entered is not an integer.")
except ZeroDivisionError:
    print("Division by zero is not allowed.")