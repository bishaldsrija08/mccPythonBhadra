"""
54321
5432
543
54
5
"""

row = 5
for i in range(1, row + 1):
    for j in range(row, i - 1, -1):
        print(j, end=" ")
    print()