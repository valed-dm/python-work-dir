# The diamond problem
# The second example of the spectrum of issues that can possibly arise from multiple inheritance 
# is illustrated by a classic problem named the diamond problem. 
# The name reflects the shape of the inheritance diagram - take a look at the picture:

class A:
    pass


class B(A):
    pass


class C(A):
    pass


class D(B, C):
    pass


d = D()

# There is the top-most superclass named A;
# there are two subclasses derived from A: B and C;
# and there is also the bottom-most subclass named D, derived from B and C (or C and B, as these two variants mean different things in Python)
# Can you see the diamond there?

# Have a look at the code in the editor. The same structure, but expressed in Python.

# Some programming languages forbid multiple inheritance at all, and as a consequence, they won't let you build a diamond - this is the route that Java and C# have chosen to follow since their origins.

# Python, however, has chosen a different route - it allows multiple inheritance, and it doesn't mind if you write and run code like the one in the editor. But don't forget about MRO - it's always in charge.


# Let's rebuild our example from the previous page to make it more diamond-like, just like below:

class Top:
    def m_top(self):
        print("top")
    

class Middle_Left(Top):
    def m_middle(self):
        print("middle_left")


class Middle_Right(Top):
    def m_middle(self):
        print("middle_right")


class Bottom(Middle_Left, Middle_Right):
    def m_bottom(self):
        print("bottom")


object = Bottom()
object.m_bottom()
object.m_middle()
object.m_top()


# Note: both Middle classes define a method of the same name: m_middle().

# It introduces a small uncertainty to our sample, although we're absolutely sure that you can answer the following key question: which of the two m_middle() methods will actually be invoked when the following line is executed?

# Object.m_middle()


# In other words, what will you see on the screen: middle_left or middle_right?

# You don't need to hurry – think twice and keep Python's MRO in mind!

# Are you ready?

# Yes, you're right. The invocation will activate the m_middle() method, which comes from the Middle_Left class. The explanation is simple: the class is listed before Middle_Right on the Bottom class's inheritance list. If you want to make sure that there’s no doubt about it, try to swap these two classes on the list and check the results.

# If you want to experience some more profound impressions about multiple inheritance and precious gemstones, try to modify our snippet and equip the Upper class with another specimen of the m_middle() method, and investigate its behavior carefully.

# As you can see, diamonds may bring some problems into your life – both the real ones and those offered by Python.

