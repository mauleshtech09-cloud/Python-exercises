number=153
str_num=str(number)
power=len(str_num)
total=0

for num in str_num:
    total += int(num) ** power
    

if total == number:
    print(f"{number} is Armstrong number!")
    
else:
    print(f"{number} is not Armstrong number!")        
    
     