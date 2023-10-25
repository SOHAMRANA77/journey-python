# Variables containing strings representing numbers
a = "22"
b = "44"

# Concatenating strings (not performing arithmetic addition)
print(a + b)

# Explicitly converting strings to integers and performing addition
print(int(a) + int(b))

# Implicit typecasting: Adding a float and an integer
c = 1.6
d = 3

# The integer 'd' is implicitly converted to a float for the addition
print(c + d)

# Example: Be careful with implicit typecasting, as it can lead to unexpected results if not handled properly.
