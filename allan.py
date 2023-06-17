my_list = ["apple", "banana", "orange", "grape"]

# Accessing individual items
print(my_list[0])  # Output: "apple"
print(my_list[2])  # Output: "orange"

# Modifying an item
my_list[1] = "kiwi"
print(my_list)  # Output: ["apple", "kiwi", "orange", "grape"]

# Slicing a list
print(my_list[1:3])  # Output: ["kiwi", "orange"]
print(my_list[:2])   # Output: ["apple", "kiwi"]
print(my_list[2:])   # Output: ["orange", "grape"]
