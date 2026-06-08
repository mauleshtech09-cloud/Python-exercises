num=75869

largest=0
smallest=9

while num > 0:
    digit = num % 10
    if digit > largest:
        largest = digit
        
    if digit < smallest:
        smallest = digit
        
    num=num//10     
        
print(f"Largest Digit : {largest}")
print(f"Smallest Digit : {smallest}")        
        
        
            