# The same effect can be observed with instance variables - take a look at the second example in the editor.

# The Sub class constructor creates an instance variable named subVar, while the Super constructor does the same with a variable named supVar. As previously, both variables are accessible from within the object of class Sub.

# The program's output is:

# 12
# 11
# output

# Note: the existence of the supVar variable is obviously conditioned by the Super class constructor invocation. Omitting it would result in the absence of the variable in the created object (try it yourself).

# Testing properties: instance variables.

class Super:
    def __init__(self):
        self.supVar = 11


class Sub(Super):
    def __init__(self):
        super().__init__()
        self.subVar = 12


obj = Sub()

print(obj.subVar)
print(obj.supVar)
