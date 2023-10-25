def generator(a):
    # This is a generator function that yields values from 1 to 'a'
    for i in range(1, a + 1):
        yield i  # Yielding each value instead of returning a list


# Create a generator object 'b' by calling the generator function
b = generator(5)

# Uncommented print statements demonstrate using 'next' to iterate manually
# print(next(b))  # Uncommenting this line would print the next value from the generator
# print(next(b))
# print(next(b))
# print(next(b))
# print(next(b))

# Iterate over the generator using a for loop
# The for loop implicitly calls 'next' and iterates through the generator until it's exhausted
for j in b:
    print(j)
