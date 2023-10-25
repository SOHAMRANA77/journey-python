# Public Access Modifiers
class Employee:
    def __init__(self):
        self.name = "Soham"


a = Employee()
print("\n# Public Access Modifiers")
print(a.name)


# Private Access Modifiers
class student:
    def __init__(self):
        self.name = "Soham"
        self.__Mark = 45


a = student()
print("\n# Private Access Modifiers", "\nprint(a.__Mark)  \"__\"",
      "\t\tAttributeError: 'student' object has no attribute '__Mark'")
# print(a.__Mark)
print("# can be Access inDirectly", "it's called name mangling ")
print(a._student__Mark)


# Protected Access Modifiers
class student_name:
    def __init__(self):
        self._name = "soham rana"


class stud(student_name):
    pass


print("\n# Protected Access Modifiers", "\nprint(a._name)  \"_\"",
      """\nprint(b.name)
      ^^^^^^
AttributeError: 'stud' object has no attribute 'name'. Did you mean: '_name'?""")
a = student_name()
b = stud()
print(a._name)
print(b._name)
print(dir(a))


# Public Access Modifiers
class Employee:
    def __init__(self):
        self.name = "Soham"


a = Employee()
print("\n# Public Access Modifiers")
print(a.name)  # Accessing a public attribute directly


# Private Access Modifiers
class Student:
    def __init__(self):
        self.name = "Soham"
        self.__mark = 45  # Private attribute


a = Student()
print("\n# Private Access Modifiers")
# Trying to access private attribute directly raises an AttributeError
# print(a.__mark)

# Private attributes can be accessed indirectly using name mangling
print("# can be Access inDirectly", "it's called name mangling ")
print(a._Student__mark)  # Accessing a private attribute indirectly using name mangling


# Protected Access Modifiers
class StudentName:
    def __init__(self):
        self._name = "soham rana"  # Protected attribute


class Stud(StudentName):
    pass


print("\n# Protected Access Modifiers")
# Protected attributes can be accessed in subclasses and also directly
a = StudentName()
b = Stud()
print(a._name)  # Accessing a protected attribute directly
print(b._name)  # Accessing a protected attribute in a subclass

# You can also check the available attributes using dir()
print(dir(a))
