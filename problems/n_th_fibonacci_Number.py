def fibonacci_iterative(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

# Function to calculate the nth Fibonacci number iteratively

# Get the number of test cases
num_test_cases = int(input("Enter the number of test cases: "))

# Prompt the user to input the number of test cases

# Process each test case
for i in range(num_test_cases):
    # Iterate through each test case
    n = int(input(f"Enter the value of N for test case {i + 1}: "))
    # Prompt the user to input the value of N for the current test case
    result = fibonacci_iterative(n)
    # Call the fibonacci_iterative function to calculate the nth Fibonacci number
    print(f"For test case {i + 1}, the {n}-th Fibonacci number is {result}")
    # Print the result for the current test case
