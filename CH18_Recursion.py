#   for other(not a good) code and understanding go and read
# from problems import Factorial_of_a_Number
"""int var, 5! = 5*4*3*2*1"""


# Calculating factorial using recursion in Python

# Recursive function to calculate factorial
def factorial(n):
    """Takes an integer n and calculates its factorial (n!)."""
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial(n - 1)


# Getting user input for the number
num = int(input())

# Calling the factorial function to calculate the factorial of the input number
p = factorial(num)

# Printing the factorial result
print(f"{num}! = {p}")
