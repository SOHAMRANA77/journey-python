# Taking user input and using a match statement for pattern matching

# Getting user input for x
x = int(input())

# Using a match statement to match the value of x
match x:
    # Case for x = 0
    case 0:
        print("x is zero")

    # Case for x = 1
    case 1:
        print("x is one")

    # Case for x = 2
    case 2:
        print("x is two")

    # Default case for any other value of x
    case _:
        print("x is", x)
# Example: It's a good practice to handle non-integer inputs gracefully.
