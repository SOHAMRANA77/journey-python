def s_e_o(a):
    e = 0  # Initialize a variable to store the sum of even digits
    o = 0  # Initialize a variable to store the sum of odd digits
    for i in a:
        i = int(i)  # Convert each character to an integer
        if i % 2 == 0:
            e += i  # If the digit is even, add it to the sum of even digits
        else:
            o += i  # If the digit is odd, add it to the sum of odd digits
    return print(e, o)  # Print the sums of even and odd digits


s = input()  # Take input as a string
s_e_o(s)  # Call the function to calculate and print the sums
