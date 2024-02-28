class Point:
    # create constructor
    def __init__(self, x, y):  #magic method #instance method
        #attributes 
        self.x = x
        self.y = y

    @classmethod
    def zero(cls):
        return cls(0, 0)

    # instance method
    def draw(self): 
        print(f"Point ({self.x}, {self.y})")

        
# point = Point(0, 0, 1, "a")
# both of the above are instances methods so we can call 
# them using instance of point class, using  an object.
#we use this instance method whenever we need object references
#for example when we drawing a point we really need to work with 
#specific point object. That is why this draw method is define as 
#instance method. 
#but there are the times we don't need existing objects and that when 
#we use class method. for example
        
point = Point.zero()# note that I am using class value Point
#In this case, zero is the method that define in class level.
#when we call it. It will return point object initialize with this values
#(point = Point(1, 2))and assigning to this point = Point.zero() variable.
#In this example, we refer to .zero method as a factory method coz it is like 
#factory. It creates new object.

#There are time initialize an object is pretty complex. Everytime when you 
#create object of given type, we have to pass some magical values and we have to 
#repeat it to in several places in our programs.
#In that case, instead of passing all magical values to create an object
#we can define factory method that will return an object with this values-Point(0, 0, 1, "a")
#In this way you can move this complexity of creating this object into the factory method.
point.draw() 