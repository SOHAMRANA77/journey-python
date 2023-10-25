# Using while loops in Python

# Getting user input for i
i = int(input())

# Commented-out code: A simple while loop to print numbers from i to 5
# while i <= 5:
#     print(i)
#     i += 1

# Using a while loop to repeatedly get user input and print it until i is greater than 5
while i <= 5:
    i = int(input())
    print(i)

# Initializing a new variable 'count' to the value of i
count = i

# Using a while loop to print numbers in descending order from 'count' to 0
while count >= 0:
    print(count)
    count -= 1
else:
    print("I am inside else")

