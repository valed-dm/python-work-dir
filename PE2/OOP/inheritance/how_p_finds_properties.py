# How Python finds properties and methods
# Now we're going to look at how Python deals with inheriting methods.

# Take a look at the example in the editor. Let's analyze it:

# there is a class named Super, which defines its own constructor used to assign the object's property, named name.
# the class defines the __str__() method, too, which makes the class able to present its identity in clear text form.
# the class is next used as a base to create a subclass named Sub. The Sub class defines its own constructor, which invokes the one from the superclass. Note how we've done it: Super.__init__(self, name).
# we've explicitly named the superclass, and pointed to the method to invoke __init__(), providing all needed arguments.
# we've instantiated one object of class Sub and printed it.
# The code outputs:

# My name is Andy.
# output

# Note: As there is no __str__() method within the Sub class, the printed string is to be produced within the Super class. This means that the __str__() method has been inherited by the Sub class.

class Super_o:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "My name is " + self.name + "."


class Sub_o(Super_o):
    def __init__(self, name):
        Super_o.__init__(self, name)


obj = Sub_o("Andy")

print(obj)

# Look at the code in the editor. We've modified it to show you another method of accessing any entity defined inside the superclass.

# In the last example, we explicitly named the superclass. In this example, we make use of the super() function, which accesses the superclass without needing to know its name:

# super().__init__(name)


# The super() function creates a context in which you don't have to (moreover, you mustn't) pass the self argument to the method being invoked - this is why it's possible to activate the superclass constructor using only one argument.

# Note: you can use this mechanism not only to invoke the superclass constructor, 
# but also to get access to any of the resources available inside the superclass.

class Super:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "My name is " + self.name + "."


class Sub(Super):
    def __init__(self, name):
        super().__init__(name)
        print('you can use this mechanism not only to invoke the superclass constructor,')
        print('but also to get access to any of the resources available inside the superclass.')
        print('attribute of superclass has been accessed in subclass: -->', self.name)


obj_1 = Sub("Andy")

print(obj_1)

# Let's try to do something similar, but with properties (more precisely: with class variables).

# Take a look at the example in the editor.

# As you can see, the Super class defines one class variable named supVar, and the Sub class defines a variable named subVar.

# Both these variables are visible inside the object of class Sub - this is why the code outputs:

# 2
# 1

# Testing properties: class variables.
class Super_1:
    supVar = 1


class Sub_1(Super_1):
    subVar = 2


obj = Sub_1()

print(obj.subVar)
print(obj.supVar)
