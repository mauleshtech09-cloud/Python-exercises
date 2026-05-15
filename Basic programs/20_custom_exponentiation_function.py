# Practice Problem: Write a function called exponent(base, exp) that returns an integer value of the base raised to the power of the exponent.

# Exercise Purpose: Learn about “Accumulator Patterns.” Although Python has a built-in power operator (**), making your own version shows how repeated multiplication works and how functions return results to the main program.

def cust_expo(base,exp):
    
    num=exp
    
    result=1
    
    while num > 0:
        
        result = result * base
        
        num=num-1
        
    print(f"{base} raises power to the {exp} is : {result}")
    
    
cust_expo(2,5)        