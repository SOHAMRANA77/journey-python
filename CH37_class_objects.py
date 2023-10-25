class Person:
    name = "Soham Rana"
    occupation = "Software Developer"
    Net_worth = 230_000_000

    def info(self):
        print(f"{self.name} is a {self.occupation}")


print(Person.name)  # Soham Rana
print(Person.occupation)  # Software Developer
print(Person.Net_worth)  # 230000000

Person.name = "Sohyem"  # Change the value of the class variable name

print(Person.name)  # Sohyem

# Call the info method using class name, passing the instance as an argument (not typical usage)
print(Person.info(self=Person))  # Sohyem is a Software Developer

# Call the info method using class instance (typical usage)
person_instance = Person()
person_instance.info()  # Sohyem is a Software Developer
