# If you name a method like this: __init__, it won't be a regular method - it will be a constructor.

# If a class has a constructor, it is invoked automatically and implicitly when the object of the class is instantiated.

# The constructor:

# is obliged to have the self parameter (it's set automatically, as usual);
# may (but doesn't need to) have more parameters than just self; if this happens, the way in which the class name is used to create the object must reflect the __init__ definition;
# can be used to set up the object, i.e., properly initialize its internal state, create instance variables, instantiate any other objects if their existence is needed, etc.
# Look at the code in the editor. The example shows a very simple constructor at work.

# Run it. The code outputs:

# object
# output

# Note that the constructor:

# cannot return a value, as it is designed to return a newly created object and nothing else;
# cannot be invoked directly either from the object or from inside the class (you can invoke a constructor from any of the object's subclasses, but we'll discuss this issue later.)

class Classy:
    def __init__(self, value):
        self.var = value


obj_1 = Classy("object")

print(obj_1.var)
print(obj_1.__dict__)
