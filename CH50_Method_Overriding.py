# Define a class 'Shape' to represent a geometric shape
class Shape:
    def __init__(self, x, y):
        self.x = x  # Initialize width or radius (for circle)
        self.y = y  # Initialize height (for rectangle)

    def area(self):
        return self.x * self.y  # Calculate and return the area
        # return f"area of {self.x} * {self.y} = {self.x * self.y}"


# Define a class 'Circle' that inherits from 'Shape'
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        super().__init__(radius, radius)  # Initialize with radius as width and height

    def area(self):
        # Override the area method to calculate area of a circle
        """overwrite return f"area of {self.radius}R is {3.14 * super().area()}"""
        return f"Area of circle with radius {self.radius} is {3.14 * super().area()}"


# Create an instance of 'Shape' representing a rectangle
rectangle = Shape(25, 2)
print(f"Area of rectangle: {rectangle.area()}")

# Create an instance of 'Circle' representing a circle
circle = Circle(5)
print(circle.area())

# Output:
# Area of rectangle: 50
# Area of circle with radius 5 is 78.5
