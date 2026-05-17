# Problem Statement: Write a Python program to create a BankAccount class with a balance attribute and two methods: deposit(amount) that adds funds to the balance, and withdraw(amount) that deducts funds but prevents the balance from going below zero.

# Purpose: Learn data validation and conditional logic inside instance methods. Preventing overdraw is a real-world business rule, and implementing it here teaches you how classes can enforce constraints on their own data, a core idea behind encapsulation in OOP.

# Given Input: Starting balance of 1000, deposit 500, withdraw 200, then attempt to withdraw 2000.

class BankAccount:
    
    def __init__(self):
        
        self.balance=1000
        
        
    def deposit(self,amount):
            
            self.balance += amount
            
            print(f"Balance after depost = {self.balance}")
            
            
    def withdraw(self,amount):
        
        if amount > self.balance:
            
            print(f"Insufficient balance , cannot be withdrawn!, balance =  {self.balance}")
            
        else:    
        
            self.balance -= amount
            
            print(f"Balance after withdraw = {self.balance}")        
                            
                            
acc1=BankAccount()                            
            
acc1.deposit(500)   
acc1.withdraw(1000)         
acc1.withdraw(2000)         