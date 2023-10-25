# Initialize a global variable x with value 4
x = 4

# Print the value of the global variable x
print(f"This x is a global variable: {x}")


def hello():
    global x  # Use the global keyword to modify the global variable x
    x = 10  # Modify the value of the global variable x
    print(f"This x is a local variable within the hello() function: {x}")
    y = 2  # Define a local variable y within the hello() function
    print(f"This y is a local variable within the hello() function: {y}")

# Call the hello() function, which modifies the global variable x and defines a local variable y
hello()

# Print the value of the modified global variable x
print(f"This x is the modified global variable after calling hello(): {x}")

# Attempting to print the local variable y outside of its scope will result in a NameError
# print(y)  # Uncommenting this line will result in a NameError

"""
print(y)
          ^not a Global variable(only for hello() )
NameError: name 'y' is not defined
"""