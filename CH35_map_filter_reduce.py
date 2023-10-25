from functools import reduce


def cube(x):
    return x * x * x


print(cube(2))
list_c = [1, 2, 3, 4, 5, 6, 7, 8, 9]
new_list = []
for i in list_c:
    new_list.append(cube(i))

print(new_list)
# ####################### Map ##########################
map_list = list(map(cube, list_c))
print(map_list)
# Lambda
newl = list(map(lambda x: x * x * x, list_c))
print(newl)


# ####################### Filter ##########################
def filter5(x):
    return x <= 5


new_l = list(filter(filter5, list_c))
print(new_l)
# Lambda
newl = list(filter(lambda x: x <= 5, list_c))
print(newl)

# ####################### Reduce ##########################
"""
def lamd(x,y):
    return x + y 
"""
# from functools import reduce
sum = reduce(lambda x, y: x + y, list_c)
print(sum)


from functools import reduce

# Function to calculate the cube of a number
def cube(x):
    return x * x * x

print(cube(2))  # Result of cubing 2: 8

# Using a for loop to create a list of cubes
list_c = [1, 2, 3, 4, 5, 6, 7, 8, 9]
new_list = []
for i in list_c:
    new_list.append(cube(i))

print(new_list)  # List of cubes using a for loop

# Using map() with the cube function
map_list = list(map(cube, list_c))
print(map_list)  # List of cubes using map()

# Using map() with a lambda function to cube the elements
newl = list(map(lambda x: x * x * x, list_c))
print(newl)  # List of cubes using map() with a lambda function

# Using filter() to filter elements less than or equal to 5
def filter5(x):
    return x <= 5

new_l = list(filter(filter5, list_c))
print(new_l)  # List of elements less than or equal to 5 using filter()

# Using filter() with a lambda function to filter elements less than or equal to 5
newl = list(filter(lambda x: x <= 5, list_c))
print(newl)  # List of elements less than or equal to 5 using filter() with a lambda function

# Using reduce() to calculate the sum of the list
sum = reduce(lambda x, y: x + y, list_c)
print(sum)  # Sum of the list using reduce()
