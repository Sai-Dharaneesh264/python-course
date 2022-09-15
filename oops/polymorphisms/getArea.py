class Shape:
    def __init__(self):
        self.sides = 0
    
    def getArea(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.sides = 4

    def getArea(self):
        return (self.width * self.height)


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        self.sides = 0
    

    def getArea(self):
        return (self.radius * self.radius * 3.142)


shapes = [Rectangle(6, 10), Circle(7)]
print("Area of rectangle is:", str(shapes[0].getArea()))
print("Area of circle is:", str(shapes[1].getArea()))