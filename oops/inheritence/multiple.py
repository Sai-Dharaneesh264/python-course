#class is derived from more than one base class i.e when a class has more than one immediate parent class
class CombustEngine():
    def setTankCapacity(self, tankCapacity):
        self.tankCapacity = tankCapacity


class ElectricEngine():
    def setChargeCapacity(self, chargeCapacity):
        self.chargeCapacity = chargeCapacity



class HybridEngine(CombustEngine, ElectricEngine):
    def printDetails(self):
        print(self.tankCapacity, self.chargeCapacity, sep=", ")


car = HybridEngine()
car.setChargeCapacity('250 W')
car.setTankCapacity('20 litres')
car.printDetails()