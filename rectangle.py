from calculator import Shape

class Rectangle(Shape):
    def __init__(self,width,height):

        # validate that width and height are positive numbers
        if not isinstance(width, (int, float)) or not isinstance(height, (int, float)):
            raise TypeError("Error: the side must be a number")
        if width <= 0 or height <= 0:
            raise ValueError("Error: the side must be a positive number")

        super().__init__("Rectangle")
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * (self.height + self.width)

    def __add__(self, other):
        if not isinstance(other,Rectangle):
            raise TypeError(f"TypeError: unsupported operand type(s) " +
                            f"for +: '{other.__class__.__name__}' and 'Rectangle'")
        new_width = self.width + other.width
        new_height = self.height + other.height
        return Rectangle(new_width,new_height)


