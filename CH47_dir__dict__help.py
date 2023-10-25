# Create a list X with various numerical values, including integers and a float
X = [1, 2, 3, 6, 9, 48, 23.564]

# Print the list of attributes and methods available for the list X
print("Attributes and methods available for the list X:")
print(dir(X))

# Define a class called 'student'
class student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.hobbies = "gaming, reading, biking"

# Instantiate an object of the 'student' class
p = student("Soham", 23)

# Print the dictionary containing object attributes
print("\nDictionary containing object attributes:")
print(p.__dict__)

# Print help/documentation for the 'student' class
print("\nHelp/documentation for the 'student' class:")
print(help(student))
