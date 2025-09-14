# 🧠 Problem 3: Multiplication Table
# ❌ Buggy Code:


def table(n):
    for i in range(1, 11):
        multiply = n * i
        print(n, "x", i, "=", multiply)

table(5)

# 🔍 Bugs to Fix:
# Wrong variable multi → should be multiply