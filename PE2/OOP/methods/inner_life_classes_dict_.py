# Each Python class and each Python object is pre-equipped with a set of useful attributes which can be used to examine its capabilities.

# You already know one of these - it's the __dict__ property.

# Let's observe how it deals with methods - look at the code in the editor.

# Run it to see what it outputs. Check the output carefully.

# Find all the defined methods and attributes. Locate the context in which they exist: inside the object or inside the class.

class Classy:
    varia = 1

    def __init__(self):
        self.var = 2

    def method(self):
        pass

    def __hidden(self):
        pass


obj = Classy()

print(obj.__dict__)
print(Classy.__dict__)
