class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


# to solve the issue with comparing point objects, we need to come back here and implement a magic methode.
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


p1 = Point(1, 2)
p2 = Point(1, 2)
# print(p1 == p2) #get false coz these two objects are in different locations in memory.
# so by default python compares objects based on where they stored in memory. 
# if two variables are referencing the same object in memory they're consider equal. 
# In this example, our point objects are in two different locations even though they have the same
# attributes. let's prove this
print(id(p1))
print(id(p2))

# we see that these objects are in two different locations in memory.

# Now lets compare with p1 == p2
print(p1 == p2)


"""
However writing all this code for data classes is a little bit tedious. If you're dealing classes
that have no behavoir, no methods, they only have data, we can use a main couple instance, let me 
show you how that works. We might want to use name tuple instead. You will write less code.
And these name tuples are better then regular tuples, because here we'll have attributes inpoint objects.
"""

from collections import namedtuple

point = namedtuple("Point", ["x", "y"])
p1 = Point (x=1, y=2)
print(p1.x)
p2 = Point (x=1, y=2)
print(p1 == p2)
