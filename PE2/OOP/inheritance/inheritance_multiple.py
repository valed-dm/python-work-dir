# Multiple inheritance occurs when a class has more than one superclass. Syntactically, such inheritance is presented as a comma-separated list of superclasses put inside parentheses after the new class name - just like here:

class SuperA:
    var_a = 10

    def fun_a(self):
        return 11


class SuperB:
    var_b = 20

    def fun_b(self):
        return 21


class Sub(SuperA, SuperB):
    pass


obj = Sub()

print(obj.var_a, obj.fun_a())
print(obj.var_b, obj.fun_b())


# The Sub class has two superclasses: SuperA and SuperB. This means that the Sub class inherits all the goods offered by both SuperA and SuperB.

# The code prints:

# 10 11
# 20 21
# output

# Now it's time to introduce a brand new term - overriding.

# What do you think will happen if more than one of the superclasses defines an entity of a particular name?

class Level10:
    var = 100

    def fun(self):
        return 101


class Level20(Level10):
    var = 200

    def fun(self):
        return 201


class Level30(Level20):
    pass


obj = Level30()

print(obj.var, obj.fun())

# Let's analyze the example in the editor.

# Both, Level1 and Level2 classes define a method named fun() and a property named var. Does this mean that the Level3 class object will be able to access two copies of each entity? Not at all.

# The entity defined later (in the inheritance sense) overrides the same entity defined earlier. This is why the code produces the following output:

# 200 201
# output

# As you can see, the var class variable and fun() method from the Level2 class override the entities of the same names derived from the Level1 class.

# This feature can be intentionally used to modify default (or previously defined) class behaviors when any of its classes needs to act in a different way to its ancestor.

# We can also say that Python looks for an entity from bottom to top, and is fully satisfied with the first entity of the desired name.

# How does it work when a class has two ancestors offering the same entity, and they lie on the same level? In other words, what should you expect when a class emerges using multiple inheritance? Let's look at this.