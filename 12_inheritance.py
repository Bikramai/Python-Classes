class Animal:
    def __init__(self): #constructor 
        self.age = 1 # age attribute

    def eat(self):
        print("eat")


# Animal: Parent, Base class
# Mammal: Child, Sub class
class Mammal(Animal): #Inheritance in action
    def walk(self):
        print("walk")

# Animal: Parent, Base class
# Fish: Child, sub class
class Fish(Animal): #Inheritance in action
    def swim(self):
        print("swim")

m = Mammal()
m.eat()
print(m.age)

#Here in above code we have repeated or duplicated each method in both this classes.
#this repeated method in programming is bad practice is know as 
# DRY = Don't Repeat Youself
# in future if we have bugs we have to fix in multipe places or similarly if we need to change
# the behavour then again we have to change in multiple places.
# In programming we have a concept called DRY- Don't Repeat Yourself.
        
# To solve this problem we have two solutions.
# We can use Inheritance or Composition

# Inheritances:-
        # Inheritances is a machanism that allows us to define common behavoiurs or common functions
# in one class and inheritance them in other classes.

# This inheritance are not limited to methods, we can also inheritance to attributes of the base class.
#

  