# There is also a Python operator worth mentioning, as it refers directly to objects - here it is:

# object_one is object_two


# The is operator checks whether two variables (object_one and object_two here) refer to the same object.

# Don't forget that variables don't store the objects themselves, but only the handles pointing to the internal Python memory.

# Assigning a value of an object variable to another variable doesn't copy the object, but only its handle. This is why an operator like is may be very useful in particular circumstances.

# Take a look at the code in the editor. Let's analyze it:

# there is a very simple class equipped with a simple constructor, creating just one property. The class is used to instantiate two objects. The former is then assigned to another variable, and its val property is incremented by one.
# afterward, the is operator is applied three times to check all possible pairs of objects, and all val property values are also printed.
# the last part of the code carries out another experiment. After three assignments, both strings contain the same texts, but these texts are stored in different objects.
# The code prints:

# False
# False
# True
# 1 2 1
# True False
# output

# The results prove that object_1 and object_3 are actually the same objects, while string_1 and string_2 aren't, despite their contents being the same.

class SampleClass:
    def __init__(self, val):
        self.val = val


object_1 = SampleClass(0)
object_2 = SampleClass(2)
object_3 = object_1
object_3.val += 1

print(object_1 is object_2)
print(object_2 is object_3)
print(object_3 is object_1)
print(object_1.val, object_2.val, object_3.val)

string_1 = "Mary had a little "
string_2 = "Mary had a little lamb"
string_1 += "lamb"

print(string_1 == string_2, string_1 is string_2)
