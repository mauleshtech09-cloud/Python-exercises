number = int (input("Enter number : "))

temp=number
rev_number= 0

while number > 0:
    digit = number % 10
    rev_number=(rev_number * 10) + digit
    number = number // 10
    
if temp == rev_number :
    print(f"{temp} is Pallindrome!") 
    
else:
    print(f"{temp} is not palllindrome!")       
    
    
    
    
    