# Problem Statement: Write a Python program to create a Light class with three methods: turn_on() that switches the light on, turn_off() that switches it off, and status() that reports whether the light is currently on or off.

# Purpose: This exercise models a simple stateful object, where the object remembers and changes its own condition over time. It introduces the concept of state management within a class, a pattern found everywhere from UI components and IoT devices to game objects and workflow engines.


class Light:

    def __init__(self):

        self.is_on = False

    def Turn_on(self):
        self.is_on = True

    def Turn_off(self):
        self.is_on = False

    def status_check(self):
        if self.is_on == True:
            print("Light is ON!")

        elif self.is_on == False:
            print("Light is OFF!")

        else:
            print("Something went wrong!")
            
light1=Light()      

light1.status_check()

light1.Turn_on()      
light1.status_check()

light1.Turn_off()
light1.status_check()
