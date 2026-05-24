class coffeeMachine:
    def __init__(self,water,milk,coffee):
        self.water=water
        self.milk=milk
        self.coffee=coffee
        
        
    def make_latte(self):
        water_needed=200
        coffee_needed=20
        milk_needed=150
        
        if self.water >= water_needed and self.coffee >= coffee_needed and self.milk >= milk_needed:
            self.water -= water_needed 
            self.coffee -= coffee_needed 
            self.milk -= milk_needed 
                
            print("Here is your Latte!")
            print(f"Water remaining = {self.water} coffee remaining = {self.coffee} milk remaining = {self.   milk}")
            
        else:
            print("Not enough resources to make a latte!")    
                
order1=coffeeMachine(500,500,40)

order1.make_latte()  
order1.make_latte()  
order1.make_latte()  
        
                    