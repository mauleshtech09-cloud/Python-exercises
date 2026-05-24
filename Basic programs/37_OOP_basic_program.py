class Car:
    
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
        
    def start_engine(self):
        print(f"The {self.year} {self.make} {self.model} is Running.....")
        
toyota=Car("Toyota","Fortuner",2007)
toyota.start_engine()           