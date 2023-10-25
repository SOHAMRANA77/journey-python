# Take the principal amount as input from the user
p = int(input("Enter the principal amount: "))

# Take the rate of interest as input from the user
r = float(input("Enter the rate of interest: "))

# Take the time in years as input from the user
t = int(input("Enter the time in years: "))

# Calculate the simple interest using the formula: Interest = (Principal * Rate * Time) / 100
interest = p * r * t / 100

# Print the calculated interest as an integer
print("Simple Interest:", int(interest))
