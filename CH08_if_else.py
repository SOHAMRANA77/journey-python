# Taking user input for age and performing conditional checks

# Getting user input for age
a = int(input("Enter your age: "))

# Printing the entered age
print("Your age is:", a)

# Checking age against conditions and providing appropriate output
if a > 100:
    print("No")
elif a >= 18:
    print("You can drive")
else:
    print("You can't drive")

# Nested if-else to classify a number

# Getting user input for a number
b = int(input("Enter a number: "))

# Checking the number against conditions and providing appropriate output
if b < 0:
    print(b, "is a negative number")
elif b > 0:
    if b <= 10:
        print(b, "is between 1-10")
    elif 10 < b <= 20:
        print(b, "is between 11-20")
    else:
        print(b, "is greater than 20")
else:
    print(b, "is zero")
# Example: Consider handling non-integer input for age and number gracefully.
