import functools
import time


# Fibonacci function using LRU cache
@functools.lru_cache(maxsize=10)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


# Calculate the 11th Fibonacci number using the Fibonacci function
a = fibonacci(11)
print(a)  # Print the 11th Fibonacci number


# Function with a sleep delay simulating a time-consuming task
@functools.lru_cache(maxsize=None)
def time_consuming_function(n):
    time.sleep(5)
    return n * 5


# Test the time-consuming function with different inputs
print(time_consuming_function(1))  # Calls the function, takes 5 seconds
print("second = 5")
print(time_consuming_function(2))  # Uses the cached result, takes some seconds
print("second = 10")
print(time_consuming_function(3))  # Uses the cached result, takes some seconds
print("second = 15")
print(time_consuming_function(1))  # Uses the cached result, prints immediately
print("second = 5")
print(time_consuming_function(2))  # Uses the cached result, prints immediately
print("second = 10")
print(time_consuming_function(3))  # Uses the cached result, prints immediately
print("second = 15")
print(time_consuming_function(31))  # Calls the function, takes some seconds
print("second = 20")
