# Write a program to input 3 digits as integers and  calculate their sum and average.

# Input three digits
num1 = int(input("Enter first digit: "))
num2 = int(input("Enter second digit: "))
num3 = int(input("Enter third digit: "))

sum  = num1 + num2 + num3
average = sum / 3

# Display the results
print(f"Sum: {sum}")
print(f"Average: {average}")