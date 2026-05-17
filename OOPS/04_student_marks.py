# Problem Statement: Write a Python program to create a Student class that stores a student’s name and a list of marks. Add a method average() that calculates and returns the average of all marks.

# Purpose: This exercise shows how instance attributes can store complex data types such as lists, not just simple values. It also practices combining OOP with list operations and arithmetic, a pattern common in gradebooks, dashboards, and reporting tools.


class Student :
    
    def __init__(self,name,mark):
        
        self.name=name
        self.marks=mark

    def Average(self):
        
        return sum(self.marks) / len(self.marks)
    
    
s1=Student("Maulesh",[99,98,100,96,95])   

print(f"Name = {s1.name}  Average = {s1.Average()}") 
    