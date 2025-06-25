from rectangle import Rectangle
from square import Square
from triangle import Triangle
from circle import Circle
from hexagon import Hexagon

class Menu:

    @staticmethod
    def print_menu():
        print("\n======= Shape Operations Menu =======")
        print("1. Create and display a shape")
        print("2. Compare two shapes (==, <)")
        print("3. Add areas of two shapes (+)")
        print("4. Exit")
        print("=====================================")

    @staticmethod
    def handle_choice(choice):
        try:
            if choice == "1":
                shape = Menu.get_valid_shape()
                print("\n--- Shape Details ---")
                print(repr(shape))
                print(shape)
                print("----------------------")

            elif choice == "2":
                print("\nEnter first shape:")
                shape1 = Menu.get_valid_shape()
                print("\nEnter second shape:")
                shape2 = Menu.get_valid_shape()

                print(f"\nComparison Results:")
                print(f"{shape1} == {shape2} -> {shape1 == shape2}")
                print(f"{shape1} < {shape2} -> {shape1 < shape2}")


            elif choice == "3":
                print("\nEnter first shape:")
                shape1 = Menu.get_valid_shape()
                print("\nEnter second shape:")
                shape2 = Menu.get_valid_shape()
                print(f"\nSum of areas: {shape1} + {shape2} = {shape1 + shape2}")

            elif choice == "4":
                print("\nExiting... Goodbye!")
                return False

            else:
                print("Invalid choice, please try again.")

        except Exception as e:
            print(f"Error: {e}")

        return True

    @staticmethod
    def get_valid_shape():
        while True:
            shape = Menu.create_shape()
            if shape:
                return shape

    @staticmethod
    def create_shape():
        print("\nChoose shape type:")
        print("1. Square")
        print("2. Rectangle")
        print("3. Triangle")
        print("4. Circle")
        print("5. Hexagon")
        choice = input("Your choice: ")
        try:
            if choice == "1":
                side = float(input("Enter side length: "))
                return Square(side)
            elif choice == "2":
                width = float(input("Enter width: "))
                height = float(input("Enter height: "))
                return Rectangle(width, height)
            elif choice == "3":
                a = float(input("Enter base: "))
                b = float(input("Enter height: "))
                return Triangle(a, b)
            elif choice == "4":
                radius = float(input("Enter radius: "))
                return Circle(radius)
            elif choice == "5":
                side = float(input("Enter side length: "))
                return Hexagon(side)
            else:
                print("Invalid choice.")
        except Exception as e:
            print(f"Error creating shape: {e}")
        return None