# Practice Problem: Read an existing file test.txt and store every line as an individual element in a Python list.

# Exercise Purpose: It’s the first step in “Data Parsing”, taking raw text from a disk and converting it into a structured format (a list) that Python can easily sort, filter, or search.

list1=[]
with open ("test.txt","r") as f:
    data=f.read()
    chunked_data=data.split()
    
    for i in chunked_data:
        list1.append(i)
        
print(list1)        