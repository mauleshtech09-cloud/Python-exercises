income=int(input("Enter income : "))

tax_payable=0

if income <= 10000:
    
    tax_payable=0
    
    
elif income <= 20000:
    
    tax_payable=(income - 10000) * 10 / 100    
    
    
else:
    
    tax_payable= 0 + (10000 * 10 / 100)
    
    
    tax_payable += (income - 20000) * 20 / 100 
    
print(f"Total tax payable = {tax_payable}")
    