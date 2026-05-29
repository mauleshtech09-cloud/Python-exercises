class Vehicle:
    def __init__(self,base_fare):
        self.base_fare=base_fare
        
        
class Taxi(Vehicle):
    def __init__(self,base_fare):
        super().__init__(base_fare)
        self.maintainance = base_fare * 0.10
        
        
    def total_fare(self):
        total_fare = self.base_fare + self.maintainance
        return total_fare

v2=Taxi(500)
print(v2.total_fare())                    