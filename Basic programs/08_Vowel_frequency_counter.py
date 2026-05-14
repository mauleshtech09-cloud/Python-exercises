# Practice Problem: Write a program to count the total number of vowels (a, e, i, o, u) present in a given sentence.

# Exercise Purpose: This exercise introduces “Membership Testing.” By checking if a character belongs to a specific group (the vowels), you learn how to filter data based on categories. This is a fundamental step toward building text-analysis tools or spam filters.

# str1=input("Enter what you want : ")

# vowels=['a','e','i','o','u','A','E','I','O','U']

# vowel_count=0

# for char in str1:
    
#     if char in vowels: 
#         vowel_count+=1
    
    
# print(f"Total vowels in given string  = {vowel_count}")    
    
    
str1=input("Enter what you want : ")

vowels="aeiou"

vowel_count=0

for char in str1.lower():
    
    if char in vowels: 
        vowel_count+=1
    
    
print(f"Total vowels in given string  = {vowel_count}")    
        
    