# rows=int(input("Enter Rows : "))

# for i in range (rows):
    
#     for j in range(i,rows):
#         print('  ',end ="")
        
#     for j in range(i+1):
#         print("*", end =" ")
        
#     print()

rows = int(input("Enter Rows: "))

for i in range(rows):
    for j in range(i):
        print('  ',end="")
        
    for j in range(i,rows):
        print('*', end =" ")    
    
    print()    
 