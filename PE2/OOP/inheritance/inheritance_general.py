# It's now possible to formulate a general statement describing Python's behavior.

# When you try to access any object's entity, Python will try to (in this order):

# find it inside the object itself;
# find it in all classes involved in the object's inheritance line from bottom to top;
# If both of the above fail, an exception (AttributeError) is raised.


# The first condition may need some additional attention. As you know, all objects deriving from a particular class may have different sets of attributes, and some of the attributes may be added to the object a long time after the object's creation.

# The example in the editor summarizes this in a three-level inheritance line. Analyze it carefully.

# All the comments we've made so far are related to single inheritance, when a subclass has exactly one superclass. This is the most common situation (and the recommended one, too).

# Python, however, offers much more here. In the next lessons we're going to show you some examples of multiple inheritance.

class Level1:
    variable_1 = 100

    def __init__(self):
        self.var_1 = 101

    def fun_1(self):
        return 102


class Level2(Level1):
    variable_2 = 200

    def __init__(self):
        super().__init__()
        self.var_2 = 201

    def fun_2(self):
        return 202


class Level3(Level2):
    variable_3 = 300

    def __init__(self):
        super().__init__()
        self.var_3 = 301

    def fun_3(self):
        return 302


obj = Level3()

print(obj.variable_1, obj.var_1, obj.fun_1())
print(obj.variable_2, obj.var_2, obj.fun_2())
print(obj.variable_3, obj.var_3, obj.fun_3())
