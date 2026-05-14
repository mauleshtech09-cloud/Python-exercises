# Practice Problem: Write a function to return True if the first and last number of a given list is the same. If the numbers are different, return False.


# Exercise Purpose: This exercise introduces “Collection Indexing” and “Boolean Flags.” Comparing data structure boundaries is common in pattern matching and data integrity checks.


def compare_list(list1):
    
    f_idx=list1[0]
    l_idx=list1[-1]
    
    if f_idx == l_idx:
        
        return True
    
    else:
        
        return False
         

li1=[40,20,30,40]

print(compare_list(li1))
