from abc import ABC, abstractmethod
import math

class Shape(ABC):
    def __init__(self,name):
        self.name = name

    @abstractmethod
    def get_area(self):
        pass

