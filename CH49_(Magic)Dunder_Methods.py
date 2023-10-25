"""
Employee class defines custom special methods:

__init__: Initializes an instance with a name.
__len__: Returns the length of the employee's name.
__str__: Returns a string representation of the employee's name.
__repr__: Returns a string representation that, if executed, would create a new instance.
__call__: Allows the instance to be callable.
MyClass class also defines custom special methods:

__init__: Initializes an instance with a value.
__str__: Returns a string representation of the instance.
__repr__: Returns a string representation that, if executed, would create a new instance.
__len__: Returns the length of the value.
__getitem__: Allows accessing elements of the value using indexing.
__eq__: Checks if two instances are equal.
"""

class Employee:
    def __init__(self, name):
        self.name = name

    def __len__(self):
        i = 0
        for c in self.name:
            i += 1
        return i

    def __str__(self):
        return f"the name of Employee is {self.name}!!!!"

    def __repr__(self):
        return f"class Employee('{self.name}')"

    def __call__(self):
        return "Hii, this Class is about>>>"


e = Employee("Sohyem")
print(e.name, "the length(__len__) is ", len(e))
print(str(e))
# print(e.__repr__())
print(repr(e))
print(e())


class MyClass:
    def __init__(self, value):
        """Initializer/Constructor - Initializes an instance of MyClass."""
        self.value = value

    def __str__(self):
        """String Representation - Returns a string representation of the instance."""
        return f"MyClass instance with value: {self.value}"

    def __repr__(self):
        """Representation - Returns a string representation that, if executed, would create a new instance."""
        return f"MyClass({self.value})"

    def __len__(self):
        """Length - Returns the length of the value."""
        return len(self.value)

    def __getitem__(self, index):
        """Get Item - Allows accessing elements of the value using indexing."""
        return self.value[index]

    def __eq__(self, other):
        """Equality - Checks if two instances are equal."""
        return self.value == other.value


# Create an instance of MyClass
my_instance = MyClass("Hello, World!")
print("\n")
# Example of __str__
print("\nUsing __str__:", str(my_instance))

# Example of __repr__
print("Using __repr__:", repr(my_instance))

# Example of __len__
print("Length of value:", len(my_instance))

# Example of __getitem__
print("Character at index 7:", my_instance[7])

# Create another instance for equality comparison
my_instance2 = MyClass("Hello, World!")

# Example of __eq__
print("Are instances equal?", my_instance == my_instance2)
