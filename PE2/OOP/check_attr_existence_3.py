# Don't forget that the hasattr() function can operate on classes, too. You can use it to find out if a class variable is available, just like here in the example in the editor.

# The function returns True if the specified class contains a given attribute, and False otherwise.

# Can you guess the code's output? Run it to check your guesses.


# And one more example - look at the code below and try to predict its output:

class ExampleClass:
    a = 1
    attr = 1

    def __init__(self):
        self.b = 2


example_object = ExampleClass()

print(hasattr(example_object, 'b'))
print(hasattr(example_object, 'a'))
print(hasattr(ExampleClass, 'b'))
print(hasattr(ExampleClass, 'a'))

print('-----------------')

print(hasattr(ExampleClass, 'attr'))
print(hasattr(ExampleClass, 'prop'))
