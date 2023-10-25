"""
Hybrid Inheritance:
Classes: Hybrid, Human, Person, Program, Student Explanation: This forms a hybrid inheritance, where Hybrid is the
base class, and Human, Person, and Program inherit from Hybrid. Student then inherits from both Person and Program.
Hybrid defines a method to display a diagram of the inheritance structure. Human, Person, and Program represent
different aspects of a student: human details, personal details, and program details. Student combines human,
personal, and program details to show the complete information of a student.

Hierarchical Inheritance:
Classes: Hierarchical, Animal, Dog, Cat Explanation: This forms a hierarchical inheritance, where Hierarchical is the
base class, and Animal, Dog, and Cat inherit from Hierarchical. Each animal type inherits from Animal. Hierarchical
defines a method to display a diagram of the inheritance structure. Animal represents generic animal details. Dog and
Cat represent specific types of animals, each adding specific details like breed and color. The code creates
instances of Student, Dog, and Cat, and then calls their respective show_details methods to display the details based
on the inheritance hierarchy.

"""
# Example of Hybrid Inheritance
class Hybrid:
    def show(self):
        print("# Example of Hybrid Inheritance")
        print("\t\t\t\t\t\tHUMAN")
        print("\t\t\t\t  / \t  |")
        print("\t\t\t\tPerson\t  |\t\tProgram")
        print("\t\t\t\t   \  \t  |\t\t   /")
        print("\t\t\t\t    \  \t  |\t\t /")
        print("\t\t\t\t\t\tStudent")



class Human(Hybrid):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_details(self):
        Hybrid.show(self)
        print("Name:", self.name)
        print("Age:", self.age)


class Person(Human):
    def __init__(self, name, age, address):
        Human.__init__(self, name, age)
        self.address = address

    def show_details(self):
        Human.show_details(self)
        print("Address:", self.address)


class Program:
    def __init__(self, program_name, duration):
        self.program_name = program_name
        self.duration = duration

    def show_details(self):
        print("Program Name:", self.program_name)
        print("Duration:", self.duration)


class Student(Person):
    def __init__(self, name, age, address, program):
        Person.__init__(self, name, age, address)
        self.program = program

    def show_details(self):
        Person.show_details(self)
        self.program.show_details()


program = Program("Computer Science", 2)
student = Student("Soham", 23, "12, india", program)
student.show_details()


class Hierarchical:
    def show(self):
        print("\n# Example of Hierarchical Inheritance")
        print("\t\t\t  Animal")
        print("\t\t\t\t |")
        print("\t----------------------------")
        print("\t|\t\t|\t\t|\t\t|\tso on..")
        print("   dogs    cats    xyz     xyz ")

class Animal(Hierarchical):
    def __init__(self, name):
        self.name = name

    def show_details(self):
        Hierarchical.show(self)
        print("Name:", self.name)

class Dog(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self, name)
        self.breed = breed

    def show_details(self):
        print("\nDOG CLASS")
        Animal.show_details(self)
        print("Species: Dog")
        print("Breed:", self.breed)

class Cat(Animal):
    def __init__(self, name, color):
        Animal.__init__(self, name)
        self.color = color

    def show_details(self):
        print("\nCAT CLASS")
        Animal.show_details(self)
        print("Species: Cat")
        print("Color:", self.color)

dog = Dog("Glody", "Golden Retriever")
dog.show_details()
cat = Cat("Luk", "Black")
cat.show_details()