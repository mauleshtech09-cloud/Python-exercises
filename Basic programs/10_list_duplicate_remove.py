# Practice Problem: Write a script that takes a list containing duplicate items and returns a new list with only unique elements.

# Exercise Purpose: This exercise teaches “Data De-duplication.” In real-world data science, datasets are often “messy” with repeating entries. Mastering the conversion between Lists (which allow duplicates) and Sets (which do not) is the fastest way to clean data.

data = [1, 2, 2, 3, 4, 4, 4, 5]

# s1=set(data) # list to set converion

# data=list(s1) # set to list conversion

data=list(set(data))

print(data)

