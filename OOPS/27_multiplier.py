# Problem Statement: Write a Python program that creates a Multiplier class which stores a factor, and implements __call__ so that an instance of the class can be invoked directly like a function to multiply a given number by that factor.

# Purpose: This exercise introduces the __call__ dunder method, which makes any object callable. This pattern is commonly used in machine learning (layer objects), decorators, and anywhere you need a stateful function-like object.


class Multiplier:
    def __init__(self,factor):
        self.factor=factor
        
        
    def __call__(self,value):
        return self.factor * value
    
    
three=Multiplier(5)
mul=three(3)
print(mul)    
nine=Multiplier(9)
mul=nine(9)
print(mul)    