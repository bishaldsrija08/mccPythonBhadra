# Write a program to input 3 sides of triangle and print area

a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))

# Calculate semi-perimeter
s = (a + b + c) / 2

# Calculate area using Heron's formula
area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
print(f"The area of the triangle is: {area}")