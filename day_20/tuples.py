# Tuples: Tuples are ordered collections of elements that are immutable.

my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)  # Output: (1, 2, 3, 4, 5)

# Access Items
print(my_tuple[0])  # Output: 1

# Update tuple

# my_tuple[0]=34
print(my_tuple)  # Output: TypeError: 'tuple' object does not support item assignment

# Loop through a tuple
for item in my_tuple:
    print(item)