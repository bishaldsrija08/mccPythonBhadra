# WAP to print the subtraction of two numbers using function with return type and with parameters.

def subtraction(a,b): # User Defined Function
    return a-b

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

result = subtraction(num1, num2)
print("The subtraction of two numbers is:", result)