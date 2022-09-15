# more than one class extends, as per the requirement of the design, from the same base class are implemented inside the base class
class Vehicle:
    def setTopSpeed(self, speed):
        self.topSpeed = speed
        print("top speed is set to", self.topSpeed)


class Car(Vehicle):
    pass


class Truck(Vehicle):
    pass


corolla = Car()
corolla.setTopSpeed(220)

volvo = Truck()
volvo.setTopSpeed(180)