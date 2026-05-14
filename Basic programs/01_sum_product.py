# Practice Problem: Write a Python function that accepts two integer numbers. If the product of the two numbers is less than or equal to 1000, return their product; otherwise, return their sum.

# Exercise Purpose: Learn basic control flow and the use of if-else statements. Understand how code decisions change output based on a mathematical threshold.

def sum_pro(a,b):
    
    if a * b <= 1000:
        
        return a * b
    
    else:
        
        return a + b
        
        
        
num1=int(input("Enter first number : "))        
num2=int(input("Enter second number : "))

print(sum_pro(num1,num2))        
        