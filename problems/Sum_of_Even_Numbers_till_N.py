def even_num(a):
    b = 0  # Initialize a variable to store the sum of even numbers
    for i in range(1, a + 1):
        if i % 2 == 0:
            b += i  # If the number is even, add it to the sum
    return b  # Return the sum of even numbers


c = int(input())  # Take user input for the limit
d = even_num(c)  # Call the function to calculate the sum of even numbers
print(d)  # Print the sum of even numbers up to the given limit
