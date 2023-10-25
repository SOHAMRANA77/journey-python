import random

# ANSI escape codes for text color
GREEN_TEXT = "\033[92m"  # Green
BLUE_TEXT = "\033[94m"   # Blue
RESET_TEXT = "\033[0m"    # Reset text color

g = f"{GREEN_TEXT}Mr. Green{RESET_TEXT}  :"  # Message format for Mr. Green
b = f"{BLUE_TEXT}Mr. Blue{RESET_TEXT}   :"  # Message format for Mr. Blue

print(g, "Hello /~")
r = input(f"{b} ").lower()  # Take input from the user and convert to lowercase
c_s = []  # List to store the modified words

while True:
    if r == "bye":
        print(f"{g} Bye!!")
        break
    elif r == "hello":
        print(f"{g} Enter your message/~")
        m = input(f"{b} ").lower()  # Take input for the message and convert to lowercase
        s = m.split()  # Split the message into words
        print(f"{g} Want to convert? Y or N/~")
        c = input(f"{b} ").lower()  # Take input for conversion
        if c == "n":
            print(f"{g} Bye!!")
            break
        else:
            for i in s:
                i = i + i[0]
                n_s = i[1:]
                front_random_chars = ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(5))
                back_random_chars = ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(5))
                new_word = ''  # Initialize a variable to store the modified word
                for n in range(1, len(n_s)):
                    if n % 2 == 0:
                        new_word = n_s[:n] + random.choice('abcdefghijklmnopqrstuvwxyz') + n_s[n:]
                code = front_random_chars + new_word + back_random_chars
                c_s.append(code)  # Append the modified word to the list
        output = " ".join(c_s)  # Join the modified words to form the output
        print(f"{g} {output}")
        break
