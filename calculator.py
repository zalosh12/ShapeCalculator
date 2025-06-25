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

    def __ne__(self, other) :
        return not isinstance(other, Shape) or self.get_area() != other.get_area()

    def __str__(self):
        return f"{self.name}, Area : {self.get_area()}, Perimeter: {self.get_perimeter()}"

    def __eq__(self, other):
        return isinstance(other,Shape) and self.get_area() == other.get_area()




