class Point:
    # create constructor
    def __init__(self, x, y):  #magic method
        #attributes 
        self.x = x
        self.y = y


    def draw(self):
        print(f"Point ({self.x}, {self.y})")

        
point = Point(1, 2) 
#create point objects supply initial value x, y coordinates(1, 2)
#to achcieve this we need constructors.
#Constructors:- which is the special method that is called magic method 
#a constructor and it executes when you create new object.

#Self:- Self is the reference to the current object.
#atributes:- object has also atributes including variables data about that object.

print(point.x) 

# In other words, class and object bondles data and functions related 
# into one unit, eg human : attributes- eyecolor, height, weight so on
# as well as function: walk, talk and so on

point.draw()

#Note:- The method that we define in class should have atleast one parameter.
#which by convention is called self and this references current point object 
#that we currently working with. When calling method of an object, we never 
#have to supply a value for parameter, python interpreter does that for us.