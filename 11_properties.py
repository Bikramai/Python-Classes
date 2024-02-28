class Product:
    def __init__(self, price):
        self.price = price

    # @classmethod # to convert class method to instances method
    @property   #when python interpreter see this code it automatically create property object call price.
    def price(self):    
        return self.__price

    # if we comment codes than it become read-only. we can only read the value of the property.
    # once set it we cannot change it 
    @price.setter # name of decorator start name of the property
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative.")
        self.__price = value

    # price = property(get_price, set_price) #property built-in function


product = Product(10)
product.price = 2
print(product.price)

# Note:- property looks like regular attributes from the outside but internally it has two methods
# a getter and a setter.  

#These two decorator we can easily create a property.