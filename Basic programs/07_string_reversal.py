# Practice Problem: Write a program that takes a string and reverses it (e.g., “Python” becomes “nohtyP”).

# Exercise Purpose: This exercise demonstrates “Sequence Slicing.” Strings in Python are sequences, and mastering the slicing syntax is a powerful shortcut for data manipulation that would take 5-10 lines of code in other languages.

str1=input("Enter a string: ")

rev_string=str1[::-1]

print(f"Reversed string = {rev_string}")