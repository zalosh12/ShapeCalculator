from rectangle import Rectangle

class Triangle(Rectangle):
    def __init__(self,base,height):

        # validate that base and height are positive numbers
        if not isinstance(base, (int, float)) or not isinstance(height, (int, float)) :
            raise TypeError("Error: the side must be a number")
        if base <= 0 or height <= 0 :
            raise ValueError("Error: the side must be a positive number")
        super().__init__(base,height)
        self.name = "Triangle"

    def get_area(self):
        return 0.5 * self.width * self.height

    def get_perimeter(self):
        return "Unknown"

    def __add__(self, other) :
        if not isinstance(other, Triangle) :
            raise TypeError(f"Error: TypeError: unsupported operand type(s) " +
                            f"for +: '{other.__class__.__name__}' and 'Triangle'")
        new_width = self.width + other.width
        new_height = self.height + other.height
        return Triangle(new_width, new_height)
