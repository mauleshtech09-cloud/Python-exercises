# Problem Statement: Write a Python program that creates objects from multiple classes and uses the built-in type() function to identify which class each object belongs to.

# Purpose: This exercise teaches you how Python tracks the type of every object at runtime. Understanding type() is essential for debugging, dynamic dispatch, and writing flexible code that reacts differently based on the type of object it receives.

class Order:
    def __init__(self,order_id,total_amount):
        self.order_id=order_id
        self.total_amount=total_amount
        
    def get_total(self):
        return self.total_amount
    
    
class discountedOrder(Order):
    
    def __init__(self,order_id,total_amount):
        super().__init__(order_id,total_amount)    
        
        
    def get_total(self):
        self.total_amount = self.total_amount * 0.90
        return self.total_amount
    
order=discountedOrder("JKS90909",1200)
print(f"Order ID : {order.order_id}")
print(f"Total Amount : {order.total_amount}")
print(f"Discounted Bill: {order.get_total()}")
        
             
    
            