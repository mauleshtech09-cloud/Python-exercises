# Problem Statement: Write a Python program to create a User class that stores a username and a password. Add a check_password(input_password) method that returns True if the input matches the stored password, and False otherwise.

# Purpose: This exercise introduces the idea of controlled access to sensitive data inside a class. Rather than exposing the password directly, the class provides a dedicated method to verify it. This pattern reflects a core principle of encapsulation in OOP, where internal data is protected and accessed only through defined interfaces.

class User:
    
    def __init__(self,username,password):
        
        self.username=username
        self.password=password
        
        
    def check_password(self,inputed_password):
        
        if inputed_password == self.password:
            
            return f"Password verified successfully! {self.password}"
        
        else:
            
            return f"Incorrect password! {inputed_password}"
    
    
    
    
user1=User("Maulesh","Admin@123")

inputed_password=input("Welcome user , Enter password : ")

print(user1.check_password(inputed_password))     