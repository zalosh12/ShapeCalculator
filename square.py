from rectangle import Rectangle

class Square(Rectangle):
    def __init__(self,side):
        super().__init__(side)
        self.name = "Square"