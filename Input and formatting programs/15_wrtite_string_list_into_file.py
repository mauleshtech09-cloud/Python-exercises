# Practice Problem: Take a list of favorite fruits and save each fruit onto a new line in a file named fruits.txt.

# Exercise Purpose: In data science or web dev, you often process data in memory (as a list) and then need to “persist” it (save it to a disk). This exercise teaches you how to export structured Python data into a permanent text format.

fruits_list=["Apple","Banana","Cherry","Date"]

with open ("fruits.txt","w") as f:
    for fruit in fruits_list:
        f.write(fruit)
        f.write("\n")
    
