# WAP to print the sum of two numbers using function.
def sum_numbers(a=10,b=8):
   return a+b

a= int(input("Enter first number: "))
b= int(input("Enter second number: "))

sum = sum_numbers(a,b)
print(sum)