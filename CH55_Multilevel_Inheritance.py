"""
Animal class is the base class, representing generic animals. It has a show method to display the name and species.

Dog class inherits from Animal and represents a dog. It has a show method that extends the Animal class's show method to
include breed.

Labrador_Retriever class inherits from Dog and represents a Labrador Retriever. It has a show method that extends the
Dog class's show method to include color.

An instance of Labrador_Retriever is created with the name "Blecky" and the color "Gold".

The show method is called on the Labrador_Retriever instance, and it prints the name, species, breed, and color.

Labrador_Retriever.mro() prints the Method Resolution Order, which shows the order in which methods are resolved in
inheritance.
"""
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def show(self):
        print(f"Name = {self.name}")
        print(f"Species = {self.species}")


class Dog(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self, name, species="Dog")
        self.breed = breed

    def show(self):
        Animal.show(self)
        print(f"Breed = {self.breed}")


class Labrador_Retriever(Dog):
    def __init__(self, name, color):
        Dog.__init__(self, name, breed="Labrador Retriever")
        self.color = color

    def show(self):
        Dog.show(self)
        print(f"Color = {self.color}")


# Create an instance of Labrador_Retriever
c = Labrador_Retriever("Blecky", "Gold")
c.show()  # Calls the show method of Labrador_Retriever

# Use Method Resolution Order (MRO) to determine the order of method invocation
print(Labrador_Retriever.mro())
