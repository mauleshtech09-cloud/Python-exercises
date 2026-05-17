# Problem Statement: Write a Python program to create a Rectangle class with length and width as instance attributes, and two methods: area() that returns the area and perimeter() that returns the perimeter.

# Purpose: Learn how to add instance methods to a class. Methods allow objects to perform operations using their own data, which is a key principle of encapsulation in OOP. Calculating geometric properties is a clean, practical context for understanding how self connects methods to instance data.


class Rectangle:
    
    def __init__(self,length,width):
        
        self.length=length
        self.width=width
        
    def area(self):
        return self.width * self.length
    
    
    def perimeter(self):
        return 2 * (self.width + self.length)
    
    
r1=Rectangle(5,20) 
area=(r1.area())
perimeter=(r1.perimeter())

print(f"Area = {area}")
print(f"Perimeter = {perimeter}")
      
      
r2=Rectangle(20,50)       
area=(r2.area())
perimeter=(r2.perimeter())

print(f"Area = {area}")
print(f"Perimeter = {perimeter}")