# What is Method Resolution Order (MRO) and why is it that not all inheritances make sense?
# MRO, in general, is a way (you can call it a strategy) in which a particular programming language scans through the upper part of a class’s hierarchy in order to find the method it currently needs. It's worth emphasizing that different languages use slightly (or even completely) different MROs. Python is a unique creature in this respect, however, and its customs are a bit specific.

# We're going to show you how Python's MRO works in two peculiar cases that are clear-cut examples of problems which may occur when you try to use multiple inheritance too recklessly. Let's start with a snippet that initially may look simple. Look at what we've prepared for you in the editor.

class Top:
    def m_top(self):
        print("top")


class Middle(Top):
    def m_middle(self):
        print("middle")


class Bottom(Middle):
    def m_bottom(self):
        print("bottom")


object = Bottom()
object.m_bottom()
object.m_middle()
object.m_top()

# We're sure that if you analyze the snippet yourself, you won't see any anomalies in it. Yes, you're perfectly right - it looks clear and simple, and raises no concerns. If you run the code, it will produce the following, predictable output:

# bottom
# middle
# top
# output


# No surprises so far. Let's make a tiny change to this code. Have a look:

class Top:
    def m_top(self):
        print("top")


class Middle(Top):
    def m_middle(self):
        print("middle")


class Bottom(Middle, Top):
    def m_bottom(self):
        print("bottom")


object = Bottom()
object.m_bottom()
object.m_middle()
object.m_top()


# Can you see the difference? It's hidden in this line:

# class Bottom(Middle, Top):

# In this exotic way, we've turned a very simple code with a clear single-inheritance path into a mysterious multiple-inheritance riddle. 
# “Is it valid?” you may ask. Yes, it is. “How is that possible?” you should ask now, 
# and we hope that you really feel the need to ask this question.

# As you can see, the order in which the two superclasses have been listed between parenthesis is compliant 
# with the code's structure: the Middle class precedes the Top class, just like in the real inheritance path.

# Despite its oddity, the sample is correct and works as expected, but it has to be stated that 
# this notation doesn’t bring any new functionality or additional meaning.

# Let's modify the code once again - now we'll swap both superclass names in the Bottom class definition. 
# This is what the snippet looks like now:

class Top:
    def m_top(self):
        print("top")


class Middle(Top):
    def m_middle(self):
        print("middle")


# class Bottom(Top, Middle):
#     def m_bottom(self):
#         print("bottom")


object = Bottom()
object.m_bottom()
object.m_middle()
object.m_top()

# To anticipate your question, we’ll say that this amendment has spoiled the code, and it won't run anymore. 
# What a pity. The order we tried to force (Top, Middle) is incompatible with the inheritance path 
# which is derived from the code's structure. Python won't like it. This is what we'll see:

# TypeError: Cannot create a consistent method resolution order (MRO) for bases Top, Middle
# output


# We think that the message speaks for itself. Python's MRO cannot be bent or violated, 
# not just because that's the way Python works, but also because it’s a rule you have to obey.

