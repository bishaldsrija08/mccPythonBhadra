# Set: Set are unordered collections of unique elements.

my_set = {1, 2, 3, 4, 5, 4, 5}
print(my_set)  # Output: {1, 2, 3, 4, 5}

# Access Items
for item in my_set:
    print(item)

# Check if an item exists
print(3 in my_set)  # Output: True

print(6 not in my_set)  # Output: True

print(1 not in my_set)  # Output: False

# Add Items
my_set.add(6)
print(my_set)  # Output: {1, 2, 3, 4, 5, 6}

# Add Sets
my_second_set = {"apple", "banana", "cherry"}
my_set.update(my_second_set)
print(my_set)  # Output: {1, 2, 3, 4, 5, 6, 'apple', 'banana', 'cherry'}

# Remove Items
my_set.remove(3)
# Discard does not raise an error if the item does not exist
my_set.discard(10)
print(my_set)  # Output: {1, 2, 4, 5, 6, 'apple', 'banana', 'cherry'}


# Loop through a set
for item in my_set:
    print(item)