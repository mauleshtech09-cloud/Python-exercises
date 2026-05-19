sentence=input("Enter anything you want : ")
contains_digit=False

for number in sentence.lower():
    
    if number.isdigit():
        contains_digit=True
        break
    
    
print(f"the string : {sentence} , contains digit : {contains_digit}")        
        
        
        