# Practice Problem: Display only those characters which are present at an even index number in given string.

# Exercise Purpose: Understand how data is stored in memory using zero-based indexing. In most languages, the first character is at position 0, the second at 1, and so on. Mastering indexing is vital for data parsing.

str1="PYnative"

even_char=(str1[0::2])

for char in even_char:
    
    print(char)