class Person:
    def __init__(self, name="SR", occupation="XY", net_worth=00):
        print("hii")
        self.name = name
        self.occupation = occupation
        self.net_worth = net_worth

    def info(self):
        print(f"{self.name} is a {self.occupation} where his net Worth is {self.net_worth}")


a = Person("soham", "Software Developer", 22)
b = Person("sohyem", "BigData Developer", 45)
a.info()
b.info()
c = Person()
c.info()
