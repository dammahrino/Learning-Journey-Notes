# Inheritance
# Using the attributes and methods from one class in another class

'''
class Person():
    def __init__(self, attribute, attribute2):
        pass
    
    
class Enemy(Person):
    def __init__(self, new_attribute, attribute, attribute2):
        super().__init__(attribute, attribute2)
        self.new_attribute = new_attribute
    
'''
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

class Enemy(Person):
    def __init__(self, weapon, first_name, last_name, health, status):
        super().__init__(first_name, last_name, health, status)
        self.weapon = weapon
        
    def hurt(self, other):
        if self.weapon == 'rock':
            other.health -= 10
        elif self.weapon == 'stick':
            other.health -= 5
        print(other.health)
        
    def insult(self, other):
        if other.health <= 80:
            print("{}, you are tired and weak".format(other.first_name))
            
    def steal(self, other):
        print("Ha ha ha, {}, I have your stuff!".format(other.first_name))
        if other.status == True:
            other.status = False
            
# Person
Maria = Person("Maria", "Cadena", 100, status=True)
Rey = Person("Rey", "Jones", 88, status=False)
Lee = Person("Lee", "Williams", 72, status=True)

# Enemy
Alex = Enemy('rock', 'Alex', 'Wayne', 75, False)

Alex.hurt(Maria)
Alex.insult(Rey)
Alex.insult(Lee)
Alex.steal(Rey)

Alex.status_change()

# Rey.steal(Alex) # Error since steal method is not declared in Person class.

# Multiple Inheritance
# When one class inherits from multiple classes, and is able to use attributes
# and methods from both classes.
# Pros
    # Ability to reuse small amounts of code in multiple classes in mixins 
# Cons
    # Order of inheritance matters
    # Inheriting from multiple classes can become quite complicated depending on the
    #   number of classes, the names of class methods, common attributes shared 
    #   among multiple parent classes
    # More maintenance
    
# MRO - Method resolution order, when using super() while having multiple inheritance.
""" 
class Animal():
    def __init__(self, sound, look):
        ...
        
class Place():
    def __init__(self, climate, lat, lon):
        ...

class Mammal(Animal, Place):
    def __init__(self, sound, look, climate, lat, lon, food):
        Animal.__init__(self, sound, look)
        Place.__init__(self, climate, lat, lon)
        self.food = food
"""

print("\n======== MULTIPLE INHERITANCE ========\n")

# Parent Class 1 
class Item():
    def __init__(self, sku):
        self.sku = sku
    
    def print_sku(self):
        print("The SKU is {}.".format(self.sku))
    
# Parent Class 2
class Garment():
    def __init__(self, section, type):
        self.section = section
        self.type = type
        
    def print_garment(self):
        print("The garment is in section {}, {}.".format(self.section, self.type))

# Child class
class Shirts(Item, Garment):
    def __init__(self, sku, section, type, name, color):
        self.name = name
        self.color = color
        Item.__init__(self, sku)
        Garment.__init__(self, section, type)
        
    def print_shirt(self):
        print("{} {} on sale!".format(self.color, self.name))
        
Blouse = Shirts("00001", 43, "Tops", "Formal Blouse", "White")

# Calling the parent methods
Blouse.print_sku()
Blouse.print_garment()
Blouse.print_shirt()

print("\n======== POLYMORPHISM (METHOD OVERRIDING) ========\n")
# When we want a child class to have a different behaviour with a method of the same
# name as the parent class.

class Enemy_Poly(Person):
    def __init__(self, weapon, first_name, last_name, health, status):
        super().__init__(first_name, last_name, health, status)
        self.weapon = weapon
    
    # Common implementation
    # def introduce(self):
    #     return super().introduce()
    
    # Overriden
    def introduce(self):
        print("You are my mortal enemy!")
        
Super_Alex = Enemy_Poly("rock", "Super", "Alex", 100, False)
Alex.introduce()
Super_Alex.introduce()