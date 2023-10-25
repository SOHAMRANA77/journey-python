# Take user input for name
name = input()

# Take user input for age and convert it to an integer
age = int(input())

# Using the .format() method to format the output string
output = 'The name of the person is {} and the age is {}.'.format(name, age)

# Using f-string to format the output string
output1 = f'The name of the person is {name} and the age is {age}.'

# Print the output using both formatting approaches
print(output)
print(output1)
