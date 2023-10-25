# Try to perform some operations based on user input
try:
    # Get user input for variables 'a' and 'b'
    a = int(input("Enter A: "))
    b = int(input("Enter B: "))

    # Perform conditional printing based on the values of 'a' and 'b'
    print(a) if a > b else print("=") if a == b else print(b)

    # Conditional assignment of 'c' based on the values of 'a' and 'b'
    c = 9 if a > b else 0

    # Print the value of 'c'
    print("c:", c)

# Handle exceptions, if any
except Exception as e:
    print("An exception occurred:", e)
