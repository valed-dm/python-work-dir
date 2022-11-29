# A class variable is a property which exists in just one copy and is stored outside any object.

# Note: no instance variable exists if there is no object in the class; a class variable exists in one copy even if there are no objects in the class.

# Class variables are created differently to their instance siblings. The example will tell you more:

class ExampleClass:
    counter = 0

    def __init__(self, val=1):
        self.__first = val
        ExampleClass.counter += 1


example_object_1 = ExampleClass()
example_object_2 = ExampleClass(2)
example_object_3 = ExampleClass(4)

print(example_object_1.__dict__, example_object_1.counter)
print(example_object_2.__dict__, example_object_2.counter)
print(example_object_3.__dict__, example_object_3.counter)

# Look:

# there is an assignment in the first list of the class definition - it sets the variable named counter to 0; initializing the variable inside the class but outside any of its methods makes the variable a class variable;
# accessing such a variable looks the same as accessing any instance attribute - you can see it in the constructor body; as you can see, the constructor increments the variable by one; in effect, the variable counts all the created objects.
# Running the code will cause the following output:

# {'_ExampleClass__first': 1} 3
# {'_ExampleClass__first': 2} 3
# {'_ExampleClass__first': 4} 3
# output

# Two important conclusions come from the example:

# class variables aren't shown in an object's __dict__ (this is natural as class variables aren't parts of an object) but you can always try to look into the variable of the same name, but at the class level - we'll show you this very soon;
# a class variable always presents the same value in all class instances (objects)
