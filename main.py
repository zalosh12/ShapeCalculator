from rectangle import Rectangle
from square import Square
from triangle import Triangle
from circle import Circle
from hexagon import Hexagon

def main():
    shapes = [
        Rectangle(3,5),
        Square(7),
        Triangle(3,4),
        Circle(3.56),
        Hexagon(4.5)
    ]

    for shape in shapes:
        print(shape.get_area())

if __name__ == "__main__":
    main()
