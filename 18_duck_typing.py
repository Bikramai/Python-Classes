class TextBox:
    def draw(self):
        print("TextBox")

class DropDownList:
    def draw(self):
        print("DropDownList")


def draw(controls):
    for control in controls:
        control.draw()



ddl = DropDownList()
# print(isinstance(ddl, UIControl))
textbox = TextBox()
draw([ddl, textbox])

#Note:- 
# Duck Typing: - walks like duck and quacks like a duck. 
# So to acheive polymorphic behaviour,  we dont necessarily need a base class like ui control, 
# Coz pyton supports duck timing. Having said that, having that ui controlled as an abstract base class
# is a good practice coz it enforces a common interface or a common contract across all it's derivatives,
# with this, we'll make sure that every kind of ui control will have a draw method.