# Problem Statement: Write a Python program that creates a Cart class that stores a list of items, and implements __len__ so that calling len(cart) returns the number of items currently in the cart.


# Purpose: This exercise introduces the __len__ dunder method, which lets your custom class integrate with Python’s built-in len() function. This is part of Python’s data model and makes your objects behave like native sequences or containers.

class Cart:
    def __init__(self):
        self.li1=[]
        
    def add_item(self,item):
        self.li1.append(item)    
        
    def __len__(self):
        return len(self.li1)    
        
c1=Cart()

c1.add_item("Apple")
c1.add_item("Banana")
c1.add_item("Kiwi")

print(f"The length of list is : {(len(c1))}")        