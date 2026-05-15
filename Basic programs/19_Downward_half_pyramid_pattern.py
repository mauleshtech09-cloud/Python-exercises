# Practice Problem: Print a downward half-pyramid pattern using stars (*).

# Exercise Purpose: Learn about reverse indexing. Controlling loop boundaries in reverse is important for algorithms that process data from end to beginning.



rows = int(input("Enter rows : "))

for i in range(rows,0,-1):
    
    for j in range(0,i):
        
        print("*",end=" ")
        
    print()      
    
    