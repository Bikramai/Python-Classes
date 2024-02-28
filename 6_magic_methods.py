class Point:
   
    def __init__(self, x, y):  #magic method
        self.x = x
        self.y = y

    #Magic method
    def __str__(self):
        return f"({self.x}, {self.y})"


    def draw(self):
        print(f"Point ({self.x}, {self.y})")

        
point = Point(1, 2)
point.__str__ 
print(str(point))