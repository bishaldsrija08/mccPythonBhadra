# Write a program to input a radius and find the area of circumference of circle
# A = πr^2
# C = 2πr
#  π = 3.14

r = float(input("Enter the radius of the circle: "))
a = 3.14*r**2
c=2*3.14*r
print(f"Area of the circle is: {a}")
print(f"Circumference of the circle is: {c}")