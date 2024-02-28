# In python, we can also use inheritance with the built-in types.

class Text(str):
    def duplicate(self):
        return self + self
    
# self represent self object which is in this case a instance of a string class. 
#extended method in builtin function
text = Text("Python")
print(text.lower())
print(text.upper())
print(text.duplicate())
print('\n')

class TraxkableList(list):
    # Techanically we are extending the append method of list class. 
    # we are not replacing it .
    def append(self, object):
        print("Append called")
        super().append(object)

list = TraxkableList()
list.append("1")