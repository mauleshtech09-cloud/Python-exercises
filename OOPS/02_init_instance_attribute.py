# Problem Statement: Write a Python program to create a Vehicle class with two instance attributes: max_speed and mileage. Create an object of the class and print both attributes.

# Purpose: Learn to define instance attributes using the __init__ constructor method. Instance attributes are unique to each object, meaning different Vehicle objects can hold different values for speed and mileage. This is a foundational concept in object-oriented programming.


class Vehicle:
    
    def __init__(self,name,max_speed,mileage):
        self.name=name
        self.max_speed=max_speed
        self.mileage=mileage
        
    def display_info(self):
        
        print(f"Name = {self.name} max speed = {self.max_speed} mileage = {self.mileage}")
        
        
BMW = Vehicle("BMW m4", "456km per hour","50km")

BMW.display_info()

            
        