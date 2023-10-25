"""
Employee class defines an employee with a name and a method show to print the name of the employee.

Gamer class defines a gamer with a game name and a method show to print the game name.

GamerEmployee class inherits from both Employee and Gamer. When a method is called on an instance of GamerEmployee, it
will first look in Employee class (due to the order of inheritance), so Employee.show method will be executed.

An instance of GamerEmployee is created with the name "Soham" and the game "Call of Duty".

The show method is called on the GamerEmployee instance, and it prints the name of the employee.

"""
class Employee:
    def __init__(self, name):
        self.name = name

    def show(self):
        print(f"The name of the Employee is {self.name}")


class Gamer:
    def __init__(self, game):
        self.game = game

    def show(self):
        print(f"The name of the game is {self.game}")


class GamerEmployee(Employee, Gamer):
    # First show of Employee will execute due to being in First position in inheritance
    def __init__(self, name, game):
        Employee.__init__(self, name=name)
        Gamer.__init__(self, game=game)


# Create an instance of GamerEmployee and call the show method
g = GamerEmployee("Soham", "Call of Duty")
g.show()  # Calls the show method of Employee because Employee is inherited first
