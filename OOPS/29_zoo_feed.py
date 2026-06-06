class Animal:
    def eat(self):
        pass

class Lion(Animal):
    def eat(self):
        return ("Lion eats Meat.") 
        
class Elephant(Animal):
    def eat(self):
        return ("Elephant eat banana.")
        
class Parrot(Animal):
    def eat(self):
        return ("Parrot eat peru.")
        
   
class Zoo:
    
    def __init__(self):
        self.animals=[]
        
    def add_animal(self,animal):
        self.animals.append(animal)
        
    def feed_all(self):
        for animal in self.animals:
            print(animal.eat()) 
            
           
zoo=Zoo()

zoo.add_animal(Lion())            
zoo.add_animal(Elephant())            
zoo.add_animal(Parrot())

zoo.feed_all()            
                      
                               