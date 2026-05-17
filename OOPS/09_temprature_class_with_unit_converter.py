# Problem Statement: Write a Python program to create a Temperature class that stores a temperature in Celsius. Add two methods: to_fahrenheit() that converts and returns the value in Fahrenheit, and to_kelvin() that converts and returns the value in Kelvin.

# Purpose: This exercise demonstrates how a class can act as a data container with built-in conversion logic. It reinforces writing multiple methods that all operate on the same instance attribute, and applies straightforward mathematical formulas in a practical scientific context.

class Temprature:
    
    def __init__(self,celsius):
        
        self.celsius=celsius

    def Farenheit_convert(self):
        
        return (self.celsius * 9/5) + 32
    
    
    def Kelvin_convert(self):
        
        return self.celsius + 273.15
    
    
celsius=int(input("Enter celsius : "))    

c1=Temprature(celsius)
print(f"{c1.celsius} celsius to  {c1.Farenheit_convert()} farenheit")
print(f"{c1.celsius} celsius to  {c1.Kelvin_convert()} kelvin")


    
            