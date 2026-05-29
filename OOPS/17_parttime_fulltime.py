class Employee:
    def __init__(self,name):
        self.name=name
        
    def calculate_pay(self):
        return 0
    
class fulltimeEmployee(Employee):
    def __init__(self,name,annual_salary):
        super().__init__(name)
        self.annual_salary=annual_salary
        
    def calculate_pay(self):
        return self.annual_salary/12
    
class ParttimeEmployee(Employee):
    def __init__(self,name,hourly_rate,hours_worked):
        super().__init__(name)
        self.hourly_rate=hourly_rate 
        self.hours_worked=hours_worked
        
    def calculate_pay(self):
        return self.hourly_rate * self.hours_worked
    
                    
emp1=fulltimeEmployee("Rahul",500000)
print(emp1.calculate_pay())
           
emp2=ParttimeEmployee("Sneha",200,12)
print(emp2.calculate_pay())           
    
    
        
        
                