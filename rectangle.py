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


