class Vehicle:
    def __init__(self,name,max_speed):
        self.name=name
        self.max_speed=max_speed
        
    def display(self):
        pass 
    
    
class Bus(Vehicle):
    
    def display(self):
        
        print(f"Vehicle : {self.name}  max_speed  : {self.max_speed}") 
        
v1=Bus("Volvo","230km/h")        
v1.display()
                  