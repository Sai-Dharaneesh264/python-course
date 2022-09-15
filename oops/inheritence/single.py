# In single inheritence, there is only class extending from another class
class Vehicle:
    a = 20
    def __init__(self, make, color, model):
        self.make = make
        self.color = color
        self.model = model
    def printDetails(self):
        print(self.make, self.color, self.model, sep=", ")


class Car(Vehicle):
    def __init__(self, make, color, model, doors):
        super().__init__(make, color, model)
        self.doors = doors
    
    def printDetails(self):
        print(self.make, self.color, self.model, self.doors, super().a, sep=", ")


car = Car('Suzuki', 'Grey', '2015', 4)

car.printDetails()