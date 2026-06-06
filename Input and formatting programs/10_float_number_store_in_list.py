# Practice Problem: Write a program that accepts 5 float numbers as input from the user and stores them in a list.

# Exercise Purpose: This exercise moves beyond single variables to “Data Structures.” It teaches how to use loops or list comprehension to efficiently handle multiple inputs and store them in a single list.


li1=[]

for i in range(6):
    number=float(input(f"Enter {i} number:  "))
    li1.append(number)
    
print(li1)    