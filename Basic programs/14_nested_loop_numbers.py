# Practice Problem: Print the following pattern where each row contains a number repeated a specific number of times based on its value.

# 1 
# 2 2 
# 3 3 3 
# 4 4 4 4 
# 5 5 5 5 5

# Exercise Purpose: Pattern printing is a classic way to learn “Nested Loops.” You coordinate an outer loop for rows and an inner loop for columns or repetitions. This improves spatial logic and control over output formatting.

rows=int(input("Enter rows: "))

for i in range(1,rows+1):
    
    for j in range(1,i+1):
        
        print(i,end=" ")
        
    print()    