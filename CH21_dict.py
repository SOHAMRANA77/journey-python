# Dictionary operations and functionalities in Python

# Creating a dictionary
person_info = {
    "first_name": "John",
    "last_name": "Doe",
    "age": 30,
    "city": "New York",
    "email": "johndoe@example.com"
}

# Printing the type and contents of the dictionary
print(type(person_info))
print(person_info)

# Accessing values in the dictionary
print(person_info["age"])  # Accessing a specific value using the key
print(person_info.get("age2"))  # Accessing a value with a non-existing key returns None

# Getting all values and keys in the dictionary
print(person_info.values())
print(person_info.keys())

# Iterating through keys and values
for keys in person_info.keys():
    print(keys, " : ", person_info[keys])

# Iterating through items (key-value pairs)
for key, value in person_info.items():
    print(key + ":\t" + str(value))

# Printing formatted key-value pairs with alignment
for key, value in person_info.items():
    key_width = max(len(key), 10)  # Calculate the width of the key
    print(f"{key}".ljust(key_width), ":", value)

# Dictionary modification operations
s1 = {1: 2, 2: 4, 3: 6, 4: 8, 5: 10}
s2 = {6: 1, 7: 3, 8: 5, 9: 7, 10: 9}
s1.pop(5)  # Remove an item with a specific key
s1.popitem()  # Remove and return an arbitrary key-value pair
del s1[1]  # Delete an item with a specific key
print(s1)
