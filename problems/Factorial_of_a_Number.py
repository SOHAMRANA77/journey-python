# Function to calculate factorial iteratively
def factorial(a):
    if a < 0:
        return "Error"
    elif a == 0:
        return 1
    else:
        result = 1
        for i in range(1, a + 1):
            result *= i
        return result


try:
    n = int(input(""))
    result = factorial(n)
    print(f"{n}! = {result}")
except ValueError:
    print("Invalid input. Please enter a non-negative integer.")

"""
Recursion

"""


# factorial(7) = 7*6*5*4*3*2*1
# factorial(6) = 6*5*4*3*2*1
# factorial(5) = 5*4*3*2*1
# factorial(4) = 4*3*2*1
# factorial(0) = 1


# factorial(n) = n * factorial(n-1)
# Recursion Example for factorial calculation
def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)


# Example usage of the recursive factorial function
print(factorial_recursive(5))

print(factorial(5))


# 5 * factorial(4)
# 5 * 4 * factorial(3)
# 5 * 4 * 3 * factorial(2)
# 5 * 4 * 3 * 2 * factorial(1)
# 5 * 4 * 3 * 2 * 1
# Recursion Example for Fibonacci sequence calculation
def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


# Example usage of the recursive Fibonacci function
for i in range(10):
    print(f"Fibonacci({i}) = {fibonacci_recursive(i)}")

# Quick Quiz: Write a program to print the Fibonacci sequence
# f(0) = 0
# f(1) = 1
# f(2) = f(1) + f(0)
# f(n) = f(n-1) + f(n-2)

# 0 1 1 2 3 5 8....
