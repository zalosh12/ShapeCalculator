from rectangle import Rectangle
from square import Square
from triangle import Triangle
from circle import Circle
from hexagon import Hexagon

def main():
    shapes = [
        Rectangle(5,5),
        Square(5),
        Triangle(3,5),
        Circle(3.56),
        Hexagon(4.5)
    ]
    # print(shapes[1] + shapes[0])
    shapes[1].visual()

    for shape in shapes:
        print(shape)
if __name__ == "__main__":
    main()
