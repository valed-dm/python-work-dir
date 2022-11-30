# As __init__ is a method, and a method is a function, you can do the same tricks with constructors/methods as you do with ordinary functions.

# The example in the editor shows how to define a constructor with a default argument value. Test it.

class Example:
    def __init__(self, value=None):
        self.var = value


obj_1 = Example("object")
obj_2 = Example()

print(obj_1.var)
print(obj_2.var)

print()

# Everything we've said about property name mangling applies to method names, too - a method whose name starts with __ is (partially) hidden.


class Classy:
    def visible(self):
        print("visible")

    def __hidden(self):
        print("hidden")


obj = Classy()
obj.visible()

try:
    obj.__hidden()
except:
    print("failed")

print()

obj._Classy__hidden()


# The code outputs:
# visible
# failed

# hidden
