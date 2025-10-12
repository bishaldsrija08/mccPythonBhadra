"""
    1
   12
  123
 1234
12345
"""

row = 5
for i in range(1, row + 1, 1):
    # Space
    for j in range(row - i):
        print(" ", end="") 
    # Number
    for k in range(1, i + 1):
        print(k, end="")
        # New Line
    print()