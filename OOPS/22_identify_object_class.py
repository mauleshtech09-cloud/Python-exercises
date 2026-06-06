# Problem Statement: Write a Python program that creates objects from multiple classes and uses the built-in type() function to identify which class each object belongs to.

# Purpose: This exercise teaches you how Python tracks the type of every object at runtime. Understanding type() is essential for debugging, dynamic dispatch, and writing flexible code that reacts differently based on the type of object it receives.

class Animal:
    pass

class Dog:
    pass

class Vehicle:
    pass


d=Dog()
a=Animal()
v=Vehicle()

print(f"Type of d is : {type(d).__name__}")
print(f"Type of a is : {type(a).__name__}")
print(f"Type of v is : {type(v).__name__}")