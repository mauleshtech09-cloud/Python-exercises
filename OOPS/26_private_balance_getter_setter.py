# Problem Statement: Write a Python program that creates a BankAccount class where the balance is stored as a private attribute __balance, and exposed safely through a @property getter and a setter that validates the value before updating it.

# Purpose: This exercise demonstrates encapsulation, one of the four pillars of OOP. Using name-mangled private attributes alongside @property lets you control how external code reads and modifies internal state, preventing invalid data from being assigned.

class Bankaccount:
    def __init__(self,initial_balance):
        self.__balance=initial_balance

    def deposit(self,amount):
        self.__balance+=amount
    
    @property
    def balance(self):
        return self.__balance        
    
    @balance.setter
    def balance(self,amount):
        if amount < 0:
            print("Amount cannot be negetive!")
    
        else:
            self.__balance = amount 
            
acc1=Bankaccount(1000)
print(f"Current Balance : ",acc1.balance)

acc1.deposit(500)
print(f"Current balance : {acc1.balance}") 

acc1.balance=-200                          
        
            
        
    
    