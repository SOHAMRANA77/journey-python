# Input the start, end, and step values
s = int(input("Enter the start value: "))
e = int(input("Enter the end value: "))
w = int(input("Enter the step value: "))

# Iterate over the range with the specified start, end, and step
for i in range(s, e, w):
    # Convert Fahrenheit to Celsius
    c = int((i - 32) * (5 / 9))

    # Print the Fahrenheit and Celsius values, separated by a tab
    print(i, c, sep="\t")
