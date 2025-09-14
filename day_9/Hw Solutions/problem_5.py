# 🧠 Problem 5: Count Down From a Number
# ❌ Buggy Code:

def countdown(start):
    for i in range(start, 0, -1):
        print(i)

count = 5
countdown(count)

# 🔍 Bugs to Fix:
# Loop won’t run: range(start, 0) → should be range(start, 0, -1)