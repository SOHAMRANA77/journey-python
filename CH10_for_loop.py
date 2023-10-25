# Looping and list manipulation in Python

# Getting user input for r
r = int(input())

# Initializing an empty list
a = []

# Looping from 1 to r with a step of 2
for i in range(1, r+1, 2):
    if i == r:
        print(i)
        a.append(i)
    else:
        print(i, end=", ")
        a.append(i)

# Printing the contents of list 'a'
print(a)

# Iterating through a list of colors and then through each character of the color
colors = ["red", "yellow", "green", "blur", "black"]
for color in colors:
    print(color)
    for i in color:
        print(i)

# Looping from 0 to 4 and printing the numbers
for i in range(5):
    print(i)
else:   # Executed after completing the for loop
    print("Sorry, 'i' left the loop normally")

# Looping from 0 to 4, printing the numbers, and breaking the loop when i reaches 3
for i in range(5):
    print(i)
    if i == 3:
        break
else:   # Executed if the for loop is broken before completing all iterations
    print("Sorry, 'i' left the loop prematurely")
