from calculator import Shape
from math import sqrt

class Hexagon(Shape):
    def __init__(self,side):
        if not isinstance(side,(int,float)):
            raise TypeError("Error: the side must be a number")
        if side <= 0:
            raise ValueError("Error: the side must be a positive number")
        super().__init__("Hexagon")
        self.side = side

    def get_area(self):
        return (3 * sqrt(3) / 2) * self.side ** 2

    def get_perimeter(self):
        return self.side * 6