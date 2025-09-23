# Write a program to input a diameter and print area of circle and circumference of circle


d = float(input("Enter the diameter of the circle: "))
r =d/2

a = 3.14 * r ** 2
c = 2 * 3.14 * r

print(f"Area of the circle: {a}")
print(f"Circumference of the circle: {c}")