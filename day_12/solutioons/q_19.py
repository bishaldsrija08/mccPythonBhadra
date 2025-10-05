# WAP to print factorial of a number.

# 5! = 5 * 4 * 3 * 2 * 1 = 120
# 10! = 10 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1 = 3628800

fact = 1
for i in range(1, 6):
    fact = fact * i
print(f"Factorial is: {fact}")