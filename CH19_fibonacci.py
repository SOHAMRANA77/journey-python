# Fibonacci sequence calculation and user interaction

# Function to calculate the nth Fibonacci number iteratively
def fibonacci_(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

# List to store the calculated Fibonacci numbers
ans = []

# List to store the input numbers for which Fibonacci is calculated
k = []

# Calculating the 6th Fibonacci number and printing it
print(fibonacci_(6))

# Getting user input for the number of Fibonacci calculations to perform
f = int(input("How many times do you want to find a Fibonacci number: "))

# Looping through the user-specified number of times to find Fibonacci numbers
for i in range(1, f + 1):
    a = int(input("Enter the number: "))
    k.append(a)
    n = fibonacci_(a)
    ans.append(n)

# Displaying the calculated Fibonacci numbers for each input number
c = 0
for i in ans:
    print(f"Fibonacci for {k[c]} is: {i}")
    c += 1
