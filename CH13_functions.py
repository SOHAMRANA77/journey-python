# Functions in Python

# Function to calculate the geometric mean of two numbers
def cal_gmean(a, b):
    return print((a * b) / (a + b))


# Function to compare numbers and print the bigger one
def numcom(a=1, b=1):
    if a > b:
        print(f"{a} is big")
    elif a == b:
        print(f"{a} and {b} are the same")
    else:
        print(f"{b} is big")


# Function to calculate the average of a variable number of arguments
def avg(*number):
    print(type(number))
    sum = 0
    for i in number:
        sum += i
    return sum / len(number)


# Function to greet a person using their first, middle, and last names
def name(**name):
    print(type(name))
    print("Hello", name["fname"], name["mname"], name["lname"])


# Sample variables
a = 8
b = 7

# Calling the functions with different parameters
cal_gmean(a, b)
numcom(a, b)
numcom(b=2, a=1)
numcom()
numcom(a=5)
c = avg(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(c)
name(fname="Soham", mname="Harish kumar", lname="Rana")
