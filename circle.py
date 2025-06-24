from calculator import Shape
from math import pi

class Circle(Shape):
    def __init__(self,radius):
        if not isinstance(radius,(int,float)):
            raise TypeError("Error: the side must be a number")
        if radius <= 0:
            raise ValueError("Error: the side must be a positive number")
        super().__init__("Circle")
        self.radius = radius

    def get_area(self):
        return pi * self.radius ** 2

    def get_perimeter(self):
        return self.radius * pi * 2

    def __add__(self, other):
        if not isinstance(other, Circle) :
            raise TypeError(f"Error: TypeError: unsupported operand type(s) "+
                            f"for +: '{other.__class__.__name__}' and 'Circle'")
        new_radius = self.radius + other.radius
        return Circle(new_radius)