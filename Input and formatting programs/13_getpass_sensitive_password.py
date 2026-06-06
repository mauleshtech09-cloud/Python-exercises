# Practice Problem: Write a script that asks a user for their username using standard input and their password using masked input (where the characters don’t appear on the screen).

# Exercise Purpose: Security is paramount. Using input() for passwords is a major vulnerability because the password remains visible in the terminal’s scrollback buffer. The getpass module is the standard way to handle sensitive credentials by suppressing local echo.

import getpass

username=input("Enter username: ")

password=getpass.getpass("Enter password: ")

if username == "Admin" and password == "kali":
    
    print(f"Login successfull for {username}")
    
else:
    
    print(f"Access denied for {username}")    
    
    