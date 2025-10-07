# WAP to find area of rectangle using function

l = float(input("Enter length of rectangle: "))
b = float(input("Enter breadth of rectangle: "))

def area_of_rectangle(l, b):
    area = l * b
    print(f"The area of the rectangle is: {area}")
area_of_rectangle(l, b)