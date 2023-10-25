# Infinite loop to take user input and process accordingly
while True:
    user_input = input("Enter the number (type 'quit' to exit): ")

    # Check if the user wants to quit
    if user_input.lower() == "quit":
        print("Ok, Bye")
        break

    try:
        u = int(user_input)

        # Check if the input number is within the range [5, 9]
        if 5 <= u <= 9:
            print(f"You have entered the number: {u}")
        else:
            # Raise a ValueError if the number is not in the specified range
            raise ValueError("The number should be between 5 to 9.")

    except ValueError as e:
        # Handle the ValueError (invalid input) and print the error message
        print(e)
