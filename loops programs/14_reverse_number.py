num=76542
reverse_number= 0 

while num > 0:
    digit = num % 10
    
    reverse_number = (reverse_number * 10) + digit
    
    num=num // 10
    
print(reverse_number)    