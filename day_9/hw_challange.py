# 🧠 Problem 1: Sum of First N Natural Numbers
# ❌ Buggy Code:

def find_sum(n):
    sum = 0
    for i in range(1, n+1):
        sum = sum + i
    prin("The sum is", sum)

number = 10
find_summ(number)

# 🔍 Bugs to Fix:
# Typo in print() → should be print()
# Wrong function name find_summ → should be find_sum


# 🧠 Problem 2: Check Even or Odd
# ❌ Buggy Code:

def check_even_odd(num):
    if number % 2 == 0:
        print "Even Number"
    else:
        print("Odd Number")

number = 7
check_even_odd(number)

# 🔍 Bugs to Fix:
# Missing parentheses in print "Even Number"
# Wrong variable name number inside the function → should use num


# 🧠 Problem 3: Multiplication Table
# ❌ Buggy Code:


def table(n):
    for i in range(1, 11):
        multiply = n * i
        print(n, "x", i, "=", multi)

table(5)

# 🔍 Bugs to Fix:
# Wrong variable multi → should be multiply


# 🧠 Problem 4: Find the Maximum of Two Numbers
# ❌ Buggy Code:

def find_max(a, b):
    if a > b:
        print a, "is greater"
    else:
        print(b, "is greater")

x = 15
y = 20
find_max(x, y)

# 🔍 Bugs to Fix:
# Missing parentheses in print a, "is greater"


# 🧠 Problem 5: Count Down From a Number
# ❌ Buggy Code:

def countdown(start):
    for i in range(start, 0):
        print(i)

count = 5
countdown(count)

# 🔍 Bugs to Fix:
# Loop won’t run: range(start, 0) → should be range(start, 0, -1)


# 📝 Tips for Students:

# Always check for correct function and variable names.

# Remember: Python 3 requires parentheses in print().

# Run the code step-by-step to find logical errors.

# Try fixing one error at a time.