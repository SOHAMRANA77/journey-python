"""
Animal is the base class representing a generic animal. It has an initializer to set the species and name and a method
sound() to print a sound message.

Dog is a subclass of Animal representing a dog. It overrides the sound() method to print a specific bark sound.

Cat is a subclass of Animal representing a cat. It overrides the sound() method to print a specific meow sound.

Instances of Animal, Dog, and Cat classes are created with different species and names.

The sound() method of each instance is called to print the respective sound based on the species.
"""
class Animal:
    def __init__(self, species, name):
        self.species = species
        self.name = name

    def sound(self):
        print(f"Sound made by {self.species} whose name is {self.name}")


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(species="Dog", name=name)
        self.breed = breed

    def sound(self):
        print(f"{self.name} ({self.breed}): Bark..bark.. ")


class Cat(Animal):
    def __init__(self, name, breed):
        super().__init__(species="Cat", name=name)
        self.breed = breed

    def sound(self):
        print(f"{self.name} ({self.breed}): Meow..meow.. ")


# Create instances of each animal type and invoke their respective sound methods
a = Animal("Dog", "Bruno")
b = Dog("Bruno", "Labrador Retriever")
c = Cat("Pitu", "British Shorthair")

# Invoke the sound method for each animal
a.sound()
b.sound()
c.sound()
