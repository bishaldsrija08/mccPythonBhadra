# Write a Python program to find the largest of three numbers using nested if-else

a = 8
b = 5
c = 3

if a>b and a>c: #a<b and a<c
    print(f"{a} is the largest number.") # smallest
elif b>a and b>c: # b<a and b<c
    print(f"{b} is the largest number.") # smallest
else:
    print(f"{c} is the largest number.") # smallest