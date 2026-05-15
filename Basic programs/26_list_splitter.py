# Practice Problem: Start with a list of 10 numbers. Iterate through them and sort them into two separate lists: one for even numbers and one for odd numbers.



numbers = [12, 7, 34, 21, 5, 10, 8, 3, 19, 2]

even=[]
odd=[]

for i in numbers:
    
    if i % 2 == 0 :
        
        even.append(i)
        
        
    elif i % 2 != 0:
        
        odd.append(i)
        
    else:
        pass
    
    
print(f"Even : {even}")            
print(f"Odd  : {odd}")            