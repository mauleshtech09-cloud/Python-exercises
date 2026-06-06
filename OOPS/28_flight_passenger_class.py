# Problem Statement: Write a Python program that creates a Passenger class and a Flight class. The Flight class should manage a list of Passenger objects and block further bookings when the seat capacity is reached.

# Purpose: This exercise models a real-world object composition scenario where one class owns and manages a collection of another class. It also teaches boundary enforcement, where business rules (capacity limits) are built directly into the class methods.

class Passenger:
    def __init__(self,name):
        self.name=name
        
class Flight:
    def __init__(self,flight_number,capacity):
        self.flight_number=flight_number
        self.capacity=capacity
        self.passenger_list=[]
        
    def book(self,passenger):
        if len(self.passenger_list) < self.capacity:
            self.passenger_list.append(passenger)
            print(f"Ticket Booked! , passenger name : {passenger.name} passenger flight : {self.flight_number} ")
            
        else:
            print("Sorry!,Limited seats")    
                                         
air_india=Flight("A1001",2)
air_india.book(Passenger("Maulesh"))
air_india.book(Passenger("Jiya"))
air_india.book(Passenger("Rohit"))

                                             