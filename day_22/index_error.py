
# List Index Error Example
a = [1,2,3]
try:
    print(a[5])
except IndexError:
    print("Index out of range")