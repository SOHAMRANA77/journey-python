class Math:
    def __init__(self, num):
        self.num = num

    def addnum(self, n):
        self.num = self.num + n

    @staticmethod   # no self,independent
    def add(c, b):
        return c + b


# Calling a static method using class name
result = Math.add(1, 2)
print(result)  # Output: 3

# Creating an instance of Math class
a = Math(7)
print(a.num)  # Output: 7

# Calling an instance method to add a number to 'num'
a.addnum(6)
print(a.num)  # Output: 13
