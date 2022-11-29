# Instance variables
# In general, a class can be equipped with two different kinds of data to form a class's properties. You already saw one of them when we were looking at stacks.

# This kind of class property exists when and only when it is explicitly created and added to an object. As you already know, this can be done during the object's initialization, performed by the constructor.

# Moreover, it can be done in any moment of the object's life. Furthermore, any existing property can be removed at any time.

# Such an approach has some important consequences:

# different objects of the same class may possess different sets of properties;
# there must be a way to safely check if a specific object owns the property you want to utilize (unless you want to provoke an exception - it's always worth considering)
# each object carries its own set of properties - they don't interfere with one another in any way.
# Such variables (properties) are called instance variables.

# The word instance suggests that they are closely connected to the objects (which are class instances), not to the classes themselves. Let's take a closer look at them.

class ExampleClass:
    def __init__(self, val = 1):
        self.first = val

    def set_second(self, val):
        self.second = val


example_object_1 = ExampleClass()
example_object_2 = ExampleClass(2)

example_object_2.set_second(3)

example_object_3 = ExampleClass(4)
example_object_3.third = 5

print(example_object_1.__dict__)
print(example_object_2.__dict__)
print(example_object_3.__dict__)

# There is one additional conclusion that should be stated here: modifying an instance variable of any object
#  has no impact on all the remaining objects. Instance variables are perfectly isolated from each other.