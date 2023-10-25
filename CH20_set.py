# s = {2, 3, 4, 5, 6, 2, 45, 4}
# set(s)
# print(type(s))
# print(s)
# info = {1.2, "soham", True, 22, 5}
# # info = {1.2 :"soham", True :22} or {}# dict
# print(info)
# print(type(info))
# k = set()
# print(type(k))
# for value in s:
#     print(value)
# s1 = {9, 8, 7, 6, 55, 4, 35, 2, 21}
# print(s.union(s1))
# print(s, s1)
# print(s.symmetric_difference(s1))  # 2.4.6 gone coman
# print(s.intersection(s1))
# print(s.intersection_update(s1))
# print(s)
# s.update(s1)
# print(s)
# Create two sets of cities
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}

# Union of sets using union() method or the | operator
cities3 = cities.union(cities2)
print(cities3)

# Alternatively, use update() method or the |= operator to update the first set with elements from the second set
cities.update(cities2)
print(cities)

# Intersection of sets using intersection() method or the & operator
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities.intersection(cities2)
print(cities3)

# Alternatively, use intersection_update() method or the &= operator to update the first set with common elements
cities.intersection_update(cities2)
print(cities)

# Symmetric Difference of sets using symmetric_difference() method or the ^ operator
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities.symmetric_difference(cities2)
print(cities3)

# Alternatively, use symmetric_difference_update() method or the ^= operator to update the first set with symmetric
# difference
cities.symmetric_difference_update(cities2)
print(cities)

# Difference of sets using difference() method or the - operator
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Seoul", "Kabul", "Delhi"}
print(cities.difference(cities2))

# Check if two sets are disjoint (no common elements)
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
print(cities.isdisjoint(cities2))   # False

# Check if two sets are disjoint (no common elements)
cities = {"Tokyo2", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid2"}
print(cities.isdisjoint(cities2))   # True

# Check if one set is a superset of another
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Seoul", "Kabul"}
print(cities.issuperset(cities2))   # False

# Check if one set is a superset of another
cities3 = {"Seoul", "Madrid", "Kabul"}
print(cities.issuperset(cities3))   # True

# Check if one set is a subset of another
cities = {"Seoul", "Madrid", "Kabul", "Delhi"}
cities2 = {"Seoul", "Kabul"}
print(cities.issuperset(cities2))   # True
print(cities2.issubset(cities))   # True

# Remove an element from a set using remove() method or discard() method (safer)
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.remove("Tokyo")
print(cities)

# Pop an arbitrary element from a set using pop() method
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
item = cities.pop()
print(cities)
print(item)

# Delete a set
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
del cities
# print(cities)  # Uncommenting this line would result in an error as the set has been deleted

# Clear all elements from a set using clear() method
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.clear()
print(cities)

# Check if an element exists in a set using the "in" keyword
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
if "Madrid" in cities:
    print("Yes")
else:
    print("No")


# Sets in Python

# Creating sets and demonstrating their properties

# Creating sets
s = {2, 3, 4, 5, 6, 2, 45, 4}
info = {1.2, "soham", True, 22, 5}
k = set()

# Performing set operations
print(s.union(info))  # Union of sets using union() method or the | operator
s.update(info)  # Update the first set with elements from the second set
print(s)

print(s.intersection(info))  # Intersection of sets using intersection() method or the & operator
s.intersection_update(info)  # Update the first set with common elements
print(s)

print(s.symmetric_difference(info))  # Symmetric Difference of sets using symmetric_difference() method or the ^ operator
s.symmetric_difference_update(info)  # Update the first set with symmetric difference
print(s)

print(s.difference(info))  # Difference of sets using difference() method or the - operator

print(s.isdisjoint(info))  # Check if two sets are disjoint (no common elements)

print(k.issuperset(s))  # Check if one set is a superset of another
print(s.issuperset(k))

print(k.issubset(s))  # Check if one set is a subset of another

s.remove(2)  # Remove an element from a set using remove() method
print(s)

item = s.pop()  # Pop an arbitrary element from a set using pop() method
print(s)
print(item)

del k  # Delete a set

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.clear()  # Clear all elements from a set using clear() method
print(cities)

# Check if an element exists in a set using the "in" keyword
if "Madrid" in cities:
    print("Yes")
else:
    print("No")
