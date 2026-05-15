# Practice Problem: Write a program to check if a given number is a palindrome. A palindrome number remains the same when its digits are reversed (e.g., 121, 545).

# Exercise Purpose: This exercise teaches “Algorithmic Reversal.” While strings are easy to reverse in Python, reversing a number mathematically using the modulo (%) and floor division (//) operators deepens understanding of how integers are stored in memory and how to manipulate digits individually.

def pallindrome(number):
    
    str_number=str(number)
    
    rev_str=str_number[::-1]
    
    
    if rev_str == str_number:
        
        print(f"Yes!, {number} is pallindome.")
        
        
    else:
        
        print(f"No!, {number} is not pallindrome.")    
        
        
        
number=int(input("Enter number : "))

pallindrome(number) 