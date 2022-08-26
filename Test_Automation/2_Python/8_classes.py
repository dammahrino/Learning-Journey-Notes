# Classes
# Grouping data and information like variables and functions, into a single organized unit.
# Single file per class
# Multiple classes can be contained in one file
# Inheritance, Multiple inheritance, polymorphism
# Class variables - usabel by all the methods in the class
# Instance variables - for use by the specific method in which the variable is declared / created

# __init__
# Creates the class with specific parameters (constructor)
# Is the first method for a class

# self
# Represents an instance of a class
# Used to represent the object that is constructed by the init method

import random

class Person:
    def __init__(self, first_name, last_name, health, status):
        "Initialize attributes to be used in/available for all of my class methos in this class, and for class objects created by this class."
        self.first_name = first_name
        self.last_name = last_name
        self.health = health
        self.status = status
        
    def introduce(self):
        "All people introduce themselves."
        print("Hello, my name is {} {}.".format(self.first_name, self.last_name))
        
    def emote(self):
        emotion = random.randint(1, 3)
        if emotion == 1:
            print("{} is happy today.".format(self.first_name))
        elif emotion == 2:
            print("{} is sad right now.".format(self.first_name))
            
    def status_change(self):
        if self.health == 100:
            print("{} is totally healthy!".format(self.first_name))
        elif self.health >= 76:
            print("{} is a little tired today.".format(self.first_name))
        elif self.health >= 51:
            print("{} feels unwell.".format(self.first_name))
        elif self.health >= 40:
            print("{} goes to the doctor.".format(self.first_name))
        else:
            print("{} is unconcious...".format(self.first_name))
            
Maria = Person("Maria", "Cadena", 100, status=True)
Rey = Person("Rey", "Jones", 88, status=False)
Lee = Person("Lee", "Williams", 72, status=True)

print("{} is my firend? {}".format(Maria.first_name, Maria.status))
print("{} is my firend? {}".format(Rey.first_name, Rey.status))

Maria.introduce()
Rey.introduce()
Lee.introduce()

Maria.status_change()
Rey.status_change()
Lee.status_change()