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