from calculator import Shape

class Rectangle(Shape):
    def __init__(self,width,height):
        super().__init__("Rectangle")
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * (self.height + self.width)
