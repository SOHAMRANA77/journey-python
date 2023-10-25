# Working with lists in Python

# Initializing an empty list
a = []

# Adding numbers from 1 to b into the list
b = 5
for i in range(1, b + 1):
    a.append(i)

# Printing list information and elements
print(type(a))
print(a)
print(a[0])
print(a[1])
print(a[len(a) - 1])
print(a[-1])

# Appending new elements to the list
a.append(11)
print(a[-1])
a.append("soham")
print(a[-1])
a.append(True)
print(a[-1])

# Checking if an element is in the list
if 7 in a:
    print(True)
else:
    print(False)

# Checking if a character is in a string
if "o" in "soham":
    print("yes")
else:
    print("no")

# List slicing
print(a)
print(a[1:4])
print(a[1::2])

# List comprehensions to generate new lists
lst = [i for i in range(1, 15)]
lst1 = [i ** i for i in range(1, 15)]
lst2 = [i for i in range(1, 15) if i % 2 == 0]
print(lst)
print(lst1)
print(lst2)

# Manipulating and accessing elements in a list
l = [1, 2, 3, 4, 5, 6, 7, 88, 0, 9, 20, 66]
l.sort(reverse=True)
l.reverse()
print(l.index(0))
print(l.count(2))
print(l)

# Creating a copy of a list and modifying it
m = l.copy()
m[0] = 11
m.insert(4, 4586)
print(m)

# Combining lists
x = [100, 568, 78, 99]
k = x + l
print(k)
l.extend(x)
print(l)
