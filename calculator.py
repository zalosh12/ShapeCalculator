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

    def __str__(self):
        return f"{self.name}, Area : {self.get_area()}, Perimeter: {self.get_perimeter()}"

    def __eq__(self, other):
        return isinstance(other,Shape) and self.get_area() == other.get_area()

