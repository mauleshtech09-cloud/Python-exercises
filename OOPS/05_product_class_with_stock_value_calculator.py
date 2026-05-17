# Problem Statement: Write a Python program to create a Product class with three instance attributes: name, price, and quantity. Add a method total_value() that returns the total stock value by multiplying price by quantity.

# Purpose: This exercise models a real-world business scenario using OOP. It reinforces how instance methods can derive new information from existing attributes, a pattern widely used in inventory management, e-commerce, and financial applications.

class Product : 
    
    def __init__(self,name,price,quantity):
        
        self.name=name
        self.price=price
        self.quantity=quantity
        
    def total_value(self):
        
        return self.price * self.quantity
    
    
    
p1=Product("Laptop",35050.67,5)  

print(f"Name = {p1.name} and total price = {p1.total_value() : .2f}")          