# Practice Problem: Write a function to remove characters from a string starting from index 0 up to n and return a new string.

# Exercise Purpose: This exercise demonstrates how to truncate data strings, a common data-cleaning task.

def string_clean(str1,idx):
    
    clean_str=str1[idx:]
    
    return clean_str

print(string_clean("PYnative",4))
print(string_clean("PYnative",2))