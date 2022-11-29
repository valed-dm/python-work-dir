# Python's attitude to object instantiation raises one important issue - in contrast to other programming languages, you may not expect that all objects of the same class have the same sets of properties.

# Just like in the example in the editor. Look at it carefully.

# The object created by the constructor can have only one of two possible attributes: a or b.

# Executing the code will produce the following output:

# 1
# Traceback (most recent call last):
#   File ".main.py", line 11, in
#     print(example_object.b)
# AttributeError: 'ExampleClass' object has no attribute 'b'
# output

# As you can see, accessing a non-existing object (class) attribute causes an AttributeError exception.

class ExampleClass:
    def __init__(self, val):
        if val % 2 != 0:
            self.a = 1
        else:
            self.b = 1


example_object = ExampleClass(1)

print(example_object.a)
print(example_object.b)
