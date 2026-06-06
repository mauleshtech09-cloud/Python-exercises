# Practice Problem: Write a program that asks the user for a filename and deletes it from the folder. Caution: This operation is permanent.

# Exercise Purpose: File system maintenance. This exercise shows you how Python can perform high-level administrative tasks. It also emphasizes the importance of “High Risk” operations and the need to always verify the user’s intent.

import os

filename=input("Choose File to delete : ")

if os.path.exists(filename):
    confirm=input((f"Are you sure you want to delete this {filename} file? (y/n): "))
    
    if confirm.lower() == "y":
        os.remove(filename)        
        print("Targeted File Deleted!")
        
    else:
        print("Opreation gets cancelled!")    
            
else:
    print("File Does not exist!")