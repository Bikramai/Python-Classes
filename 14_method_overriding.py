class Animal:
    def __init__(self): #constructor 
        print("Animal Constructor")
        self.age = 1 # age attribute

    def eat(self):
        print("eat")


# Animal: Parent, Base class
# Mammal: Child, Sub class
class Mammal(Animal): #Inheritance in action
     #method overriding
    def __init__(self): #constructor 
        print("Mammal Constructor") # to see the execution flow
        self.weight = 10 # age attribute
        super().__init__() #built-in function- to access super or base class. here in this case Animal.


    def walk(self):
        print("walk")

# Animal: Parent, Base class
# Fish: Child, sub class
class Fish(Animal): #Inheritance in action

   

    def swim(self):
        print("swim")

m = Mammal()
print(m.age) 
print(m.weight)

# Method Overriding: overriding or replacing or extending method in a base class.

# In this Implementation, we are extending __init__ method that we have defined in the Animal 
# class coz we work here in constructor Mammal than we call construtor of Animal. if we didnt
# have super().__init__().[This def __init__(self): #constructor 
        #print("Mammal Constructor") # to see the execution flow
        #self.weight = 10 # age attribute]  
# implementation is completely replace the __init__ method in Animal class.

