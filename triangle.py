from rectangle import Rectangle

class Triangle(Rectangle):
    def __init__(self,base,height):
        super().__init__(base,height)
        self.name = "Triangle"

    def get_area(self):
        return 0.5 * self.width * self.height

    def get_perimeter(self):
        return "Unknown"