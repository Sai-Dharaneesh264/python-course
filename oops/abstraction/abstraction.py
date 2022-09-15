from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass

class Square(Shape):

    def __init__(self, length):
        self.length = length

    def area(self):
        return (self.length * self.length)

    def perimeter(self):
        return (4 * self.length)

square = Square(4)

print(square.area(), square.perimeter())
