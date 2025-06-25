from calculator import Shape
from math import sqrt

class Triangle(Shape):
    def __init__(self,base,height):
        # validate that base and height are positive numbers
        if not isinstance(base, (int, float)) or not isinstance(height, (int, float)) :
            raise TypeError("Error: the side must be a number")
        if base <= 0 or height <= 0 :
            raise ValueError("Error: the side must be a positive number")
        super().__init__("Triangle")
        self.base = base
        self.height = height

    def get_area(self):
        return 0.5 * self.base * self.height

    def get_perimeter(self) :
        hypotenuse = sqrt(self.base ** 2 + self.height ** 2)
        return self.base + self.height + hypotenuse


    def __add__(self, other) :
        if not isinstance(other, Triangle) :
            raise TypeError(f"Error: TypeError: unsupported operand type(s) " +
                            f"for +: '{other.__class__.__name__}' and 'Triangle'")
        new_width = self.base + other.base
        new_height = self.height + other.height
        return Triangle(new_width, new_height)

    def __repr__(self) :
        return f"Triangle(base={self.base},height={self.height})"
