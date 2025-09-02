# WAP that takes a number as input and prints it's firts 10 multiples.

num = int(input("Enter a number: "))

for i in range(1, 11):
    multiple = num*i
    print(f"{num}x{i}={multiple}")
