class Vehicle:
    color = "white" 
    
    def __init__(self,name,speed):
        self.name=name
        self.speed=speed

    def showCar(self):
        print(f"Car : {self.name}   color : {self.color}   speed : {self.speed}")
        
v1=Vehicle("BMW",455)
v1.showCar()

v2=Vehicle("Lamborghini",333)
v2.showCar()     

v1.color="Red"           
v2.color="Red"           
        
v1.showCar()
v2.showCar()     

    