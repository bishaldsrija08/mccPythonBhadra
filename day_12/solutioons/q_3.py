# Write a Python program to convert a temperature from Celsius to Fahrenheit and Kelvin.

# K = C + 273.15
# F = (C * 9/5) + 32

c = float(input("Enter temperature in Celsius: "))

k = c+273.15
f= (c*9/5)+32

print(f"Temperature in Kelvin: {k} K")

print(f"Temperature in Fahrenheit: {f} F")