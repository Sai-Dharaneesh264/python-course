# Hybrid inheritence which is a combination of multiple and multi-level inheritence
class Engine:
    def setPower(self, power):
        self.power = power

class CombustEngine(Engine):
    def setTankCapacity(self, tankCapacity):
        self.tankCapacity = tankCapacity


class ElectricEngine(Engine):
    def setChargeCapacity(self, chargeCapacity):
        self.chargeCapacity = chargeCapacity



class HybridEngine(CombustEngine, ElectricEngine):
    def printDetails(self):
        print(self.power, self.tankCapacity, self.chargeCapacity, sep=", ")


car = HybridEngine()
car.setPower('2000 CC')
car.setChargeCapacity('250 W')
car.setTankCapacity('20 litres')
car.printDetails()