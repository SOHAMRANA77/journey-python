class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def show(self):
        print(f"Employee at {self.id} is {self.name}")


class programmer(Employee):
    def show_p(self):
        print("program class")
        print(f"Employee at {self.id} is {self.name}")


a = Employee("soham", 445468)
a.show()  # Calls the 'show' method of Employee class
# Output: Employee at 445468 is soham

a1 = programmer("Soham", 483876)
a1.show_p()  # Calls the 'show_p' method of programmer class
# Output:
# program class
# Employee at 483876 is Soham
