from rectangle import Rectangle

class Square(Rectangle):
    def __init__(self,side):
        if not isinstance(side,(int,float)):
            raise TypeError("Error: the side must be a number")
        if side <= 0:
            raise ValueError("Error: the side must be a positive number")
        super().__init__(side,side)
        self.name = "Square"

    def __add__(self, other):
        if not isinstance(other, Square) :
            raise TypeError(f"Error: TypeError: unsupported operand type(s) " +
                            f"for +: '{other.__class__.__name__}' and 'Square'")
        new_side = self.height + other.height
        return Square(new_side)
