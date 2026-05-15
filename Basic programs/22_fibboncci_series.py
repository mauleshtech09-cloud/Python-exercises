terms = int(input("Enter for how many terms you want fibonacci series : "))

num1, num2 = 0, 1

for i in range(terms):
    
    print(num1, end =" ")
    
    result= num1 + num2
    
    num1=num2
    num2=result

