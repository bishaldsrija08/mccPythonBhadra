# List
# my_list = [1, 2, 3, 4, 5]

# Dictionary
my_dict = {
    "name": "Bishal",
    "age": 22,
    "city": "Chitwan",
    "college": "IOE",
    "phone": 1234567890,
    "phone": 9876543210,  # Duplicate key; last value will be retained
}

my_dict.update({"country": "Nepal"})  # Adding a new key-value pair

my_dict["fav_color"] = "red" # Another way to add a new key-value pair

my_dict.pop("age")


for x in my_dict:
  print(x, my_dict[x])
  

copy_dict = my_dict.copy()  # Creating a shallow copy of the dictionary

# add to copy_dict
copy_dict["hobby"] = "reading"

print(copy_dict)
print(my_dict)  # Original dictionary remains unchanged