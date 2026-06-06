# Problem Statement: Write a Python program that defines a Vehicle base class and creates Bike, Truck, and Bus subclasses, each defining a unique max_speed attribute and a describe() method.

# Purpose: This exercise reinforces the concept of class hierarchies and shows how subclasses can specialise a shared blueprint with their own attribute values, reflecting how real-world transport systems are categorised.


class Vehicle:
    def __init__(self,max_speed):
        self.max_speed=max_speed
        
    def describe(self):
        print(f"{type(self).__name__} Max speed : {self.max_speed} km/h")    
        

class Bike(Vehicle):
    def __init__(self):
        super().__init__(90)
          
class Truck(Vehicle):
    def __init__(self):
        super().__init__(150)

class Bus(Vehicle):
    def __init__(self):
        super().__init__(120)
        
Vehicles=[Bike(),Truck(),Bus()]   

for v in Vehicles:
    v.describe()    