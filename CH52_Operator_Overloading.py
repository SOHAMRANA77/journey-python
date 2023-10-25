"""
The Vector class is defined with an initializer __init__ that takes three components a, b, and c.

The __str__ method is defined to provide a string representation of the vector in the form of "aa + bb + c*c".

The __add__ method is defined to handle vector addition. It takes another vector (other) as an argument and returns a
new vector that is the sum of the two input vectors.

Instances of the Vector class are created (v1 and v2).

The vectors are printed using the __str__ method.

Vector addition (v1 + v2) is performed using the __add__ method, resulting in a new vector v3.

"""
class Vector:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __str__(self):
        return f"{self.a}a + {self.b}b + {self.c}c"

    def __add__(self, other):
        # Define the addition of two vectors
        return Vector(self.a + other.a, self.b + other.b, self.c + other.c)


# Create instances of the Vector class
v1 = Vector(1, 2, 3)
v2 = Vector(5, 4, 3)

# Print the vectors
print("Vector v1:", v1)
print("Vector v2:", v2)

# Add the vectors using the __add__ method
v3 = v1 + v2

# Print the result of vector addition
print("Vector v1 + v2:", v3)
