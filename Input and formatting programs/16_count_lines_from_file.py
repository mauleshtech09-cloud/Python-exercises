# Practice Problem: Write a program that opens an existing text file and calculates exactly how many lines of text it contains.

# Exercise Purpose: This is a fundamental “Data Auditing” task. Before you process a log file or a dataset, you need to know its size. This exercise teaches you how to iterate through a file object efficiently.

line_count=0

with open ("test.txt","r") as f:
    for line in f:
        line_count+=1
        
print(line_count)        

