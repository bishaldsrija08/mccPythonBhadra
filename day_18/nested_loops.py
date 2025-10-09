# Nested loops => loops inside loops

for i in range(1,4,1):
    for j in range(1,4,1):
        print(f"i: {i}, j: {j}")
    print("Inner loop finished")
print("Outer loop finished")