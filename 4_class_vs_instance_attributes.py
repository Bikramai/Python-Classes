class Point:
    #class level attributes in the body of class 
    default_color = "red"
    # create constructor
    def __init__(self, x, y):  #magic method
        #attributes 
        self.x = x
        self.y = y

    def draw(self):
        print(f"Point ({self.x}, {self.y})")

Point.default_color = "yellow" #class level attributes shared

        
point = Point(1, 2) 
#class attributs are shared across all instances of class. if you change the value
# they change it visible to all object of types.
# In practical we will be using instances attributes most of time
print(point.default_color)
print(Point.default_color) #class level attributes shared
point.z = 10 
# we can also create attributes after object coz object in python is dyanamic
# similar like javascript. we dont have to define all the attributes in 
# a constructors. We can define later when we need them.

# Here is what important for us understand - all these attributes we define
# so far x, y, z. These are instance attributes. 

# In other words here, these are attributes belong to point instances or point objects.
# Every point objects have different point values for these attributes.
another = point(3, 4) 
print(Point.default_color) #class level attributes shared
point.draw()