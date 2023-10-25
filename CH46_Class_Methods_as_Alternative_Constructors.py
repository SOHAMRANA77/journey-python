class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @classmethod
    def fromstr(cls, string):
        name, salary = string.split('_')
        return cls(name, int(salary))

# Create an Employee instance using regular initialization
e1 = Employee("Soham", 125000)
print(e1.name)  # Soham
print(e1.salary)  # 125000

# Create an Employee instance using string and split
str1 = "SohamRana_236000"
e2 = Employee(str1.split('_')[0], int(str1.split('_')[1]))
print(e2.name)  # SohamRana
print(e2.salary)  # 236000

# Create an Employee instance using the class method
str2 = "SohamRana_236000"
e3 = Employee.fromstr(str2)
print(e3.name)  # SohamRana
print(e3.salary)  # 236000

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_string(cls, string):
        name, age = string.split(', ')
        return cls(name, int(age))

# Create a Person instance using the class method
person = Person.from_string("John Doe, 30")
print(person.name, person.age)  # John Doe 30
