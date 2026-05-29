class Animal:
    def sound(self):
        print("speaking.......")
        
class Dog(Animal):
    def sound(self):
        return("Woof!")
        
class Cat(Animal):
    def sound(self):
        return("Meow!")     
        
        
dog=Dog()
print(f"Dog says : {dog.sound() } ")  


cat = Cat()
print(f"Cat says : {cat.sound() } ")                 