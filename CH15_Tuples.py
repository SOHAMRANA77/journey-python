# Tuples in Python

# Creating a tuple
T = (1, 1, 5, 8, 8, 9, 2, 5, "soham")

# Uncommenting the line below will give an error because tuples are immutable
# T[0] = 55

# Printing tuple type and content
print(type(T), T)

# Creating single element tuples
Tu = (1)
print(type(Tu), Tu)  # This is not a tuple

Tup = (1,)  # This is a tuple with a single element
print(type(Tup), Tup)

# Accessing elements of the tuple
print(T[0])
print(T[1])
print(T[-1])

# Checking if an element is in the tuple
if 8 in T:
    print("Yes")

# Slicing a tuple
Tupl = T[1:4]
print(Tupl)

# Modifying a tuple indirectly by converting to a list
countries = ("Spain", "Italy", "India", "England", "Germany")
temp = list(countries)
temp.append("Russia")  # add item
temp.pop(3)  # remove item
temp[2] = "Finland"  # change item
countries = tuple(temp)
print(countries)

# Combining tuples
countries = ("Pakistan", "Afghanistan", "Bangladesh", "ShriLanka")
countries2 = ("Vietnam", "India", "China")
southEastAsia = countries + countries2
print(southEastAsia)

# Counting occurrences in a tuple
a = T.count(8)
print("Count of 8 in tuple is", a)

# Finding the index of an element in a tuple
Tuple = (0, 1, 2, 35, 2, 3, 1, 3, 2)
res = Tuple.index(3)
print('First occurrence of 3 is', res)
res = Tuple.index(3, 6, 8)  # Search between index 6 and 8
print('First occurrence of 3 is', res)
