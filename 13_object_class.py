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
print(isinstance(m, Animal)) #built-in function
print(isinstance(m, object))
print(issubclass(Mammal, Animal))  #built-in function - if it class derive from another class.
#let's see if Mammal is subclass of Animal
print(issubclass(Mammal, object))

# why we still get True in terminal, both case in Mammal and Animal coz Mammal inheritance 
# from Animal so instances of the mammal class is also amimal.

# let's see something interesting, in animal class we define here inheritance another class 
# called object even though we didn't add in here class Animal(object)i,e is the base class 
# for all classes in python. Every class we have directly or indirectly derive from object class.
# Here Mammal inheritance from Animal which inheritance from object.


