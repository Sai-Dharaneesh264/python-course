# when a class id derived from a class which itself is derived from another class, it is called multilevel inheritence
class Vehicle:
    def setTopSpeed(self, speeed):
        self.topSpeed = speeed
        print("top speed is set to", self.topSpeed)


class Car(Vehicle):
    def openTrunk(self):
        print("trunk is now open")


class Hybrid(Car):
    def turnOnHybrid(self):
        print("Hybrid mode is now switched on.")


priusPrime = Hybrid()
priusPrime.setTopSpeed(220)
priusPrime.openTrunk()
priusPrime.turnOnHybrid()