# Problem Statement: Write a Python program that creates a Character class with health, exp, and level attributes. The character should automatically level up and reset exp whenever accumulated experience reaches or exceeds 100.


# Purpose: This exercise shows how to embed game logic directly into a class using a method that manages state transitions. It also demonstrates how to handle overflow (excess exp after levelling up) and keep multiple related attributes in sync.

class Character:
    def __init__(self,name,health):
        self.name=name
        self.health=health
        self.exp=0
        self.level=1
        
    def gain_exp(self,amount):
        self.exp+=amount 
        
        if self.exp >= 100:
            self.exp -= 100
            self.level+=1
            
            print(f"Leveled up!, Now Level : {self.level} with Exp : {self.exp}")        
        
        else:
            print(f"Current Level : {self.level} with Exp : {self.exp}")
            
hero=Character("Maulesh",100)
hero.gain_exp(120)               
hero.gain_exp(20)               
hero.gain_exp(20)               
hero.gain_exp(20)               
hero.gain_exp(20)               
           
        
        