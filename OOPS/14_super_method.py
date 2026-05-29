class Vehicle:
    def __init__(self,name,capacity):
        self.name=name
        self.capacity=capacity
        
    def seating_capacity(self,capacity):
        print(f"{self.name} with seating capacity : {capacity}")
    
class Bus(Vehicle):
    def seating_capacity(self):
        super().seating_capacity(50)
        
v2=Bus("Bus",120)
v2.seating_capacity()    
            
    