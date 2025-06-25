from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self,name):
        self.name = name

    @abstractmethod
    def get_area(self):
        pass

    @abstractmethod
    def get_perimeter(self):
        pass

    @abstractmethod
    def __add__(self,other):
        pass

    @abstractmethod
    def __repr__(self):
        pass

    def __eq__(self, other) -> bool:
        return isinstance(other, Shape) and self.get_area() == other.get_area()

    def __ne__(self, other) -> bool:
        return not isinstance(other, Shape) or self.get_area() != other.get_area()

    def __gt__(self, other) -> bool:
        if not isinstance(other,Shape):
            raise TypeError(f"Cannot compare 'Shape' with {other.__class__.__name__}")
        return self.get_area() > other.get_area()

    def __ge__(self, other) -> bool:
        if not isinstance(other,Shape):
            raise TypeError(f"Cannot compare 'Shape' with {other.__class__.__name__}")
        return self.get_area() >= other.get_area()

    def __lt__(self, other) -> bool:
        if not isinstance(other, Shape) :
            raise TypeError(f"Cannot compare 'Shape' with {other.__class__.__name__}")
        return self.get_area() < other.get_area()

    def __le__(self, other) -> bool:
        if not isinstance(other, Shape) :
            raise TypeError(f"Cannot compare 'Shape' with {other.__class__.__name__}")
        return self.get_area() <= other.get_area()

    def __str__(self):
        return f"{self.name}, Area : {self.get_area()}, Perimeter: {self.get_perimeter()}"






