# Practice Problem: Iterate through a given list of numbers and print only those numbers which are divisible by 5.

# Exercise Purpose: This exercise teaches the use of the modulo operator (%) and loop filtering. In data processing, you often need to sift through large datasets to extract subsets that meet mathematical criteria.

num_list=[10,20,33,46,55]

for i in num_list:
    
    if i % 5 ==0:
        
        print(i,end=" ")
        
    else:
        pass
    
        
        