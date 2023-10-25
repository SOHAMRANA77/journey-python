# print(f"Class name: {type(self).__name__}")
# print(f"Method name: {self.example_method.__name__}")
# Define a parent class
class parent_class:
    def parent_method(self):
        print("This is a Parent Method from Parent Class")


# Define a child class that inherits from the parent class
class child_class(parent_class):
    def parent_method(self):
        print("\nThis is a Parent Method from Child Class")
        super().parent_method()  # Calls the parent method using super()

    def childmethod(self):
        print("This is a Child Method from Child Class")
        super().parent_method()  # Calls the parent method using super()


# Instantiate an object of the child class
c = child_class()

# Call the child method, which in turn calls the parent method
c.childmethod()
c.parent_method()
print("\n")


class Employee:
    def __init__(self, name, id):
        self.Name = name
        self.ID = id


class programmer(Employee):
    def __init__(self, name, ID, lang):
        super().__init__(name, ID)
        self.lang = lang


s = Employee("soham rana", 1)
print(s.ID, s.Name)

s1 = programmer("Sohyem", 2, "Python")
print(s1.ID, s1.Name, s1.lang)
