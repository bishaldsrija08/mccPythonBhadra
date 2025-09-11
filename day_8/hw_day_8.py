'''
Create a program that:
    - Takes a list of numbers from the user.
    - Finds the maximum, minimum, total, and average.
    - Prints the results in a formatted message.
'''

a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))
c = int(input("Enter number 3: "))
d = int(input("Enter number 4: "))
e = int(input("Enter number 5: "))
f = int(input("Enter number 6: "))
g = int(input("Enter number 7: "))

numbers = [a,b,c,d,e,f,g]

max_num = max(numbers)
min_num = min(numbers)
total = sum(numbers)
average = total / len(numbers)

print(f"Maximum: {max_num}")
print(f"Minimum: {min_num}")
print(f"Total: {total}")
print(f"Average: {average}")