# The previous example (iterator protocol) shows you a solution where the iterator object is a part of a more complex class.

# The code isn't really sophisticated, but it presents the concept in a clear way.

# Take a look at the code in the editor.

# We've built the Fib iterator into another class (we can say that we've composed it into the Class class). It's instantiated along with Class's object.

# The object of the class may be used as an iterator when (and only when) it positively answers to the __iter__ invocation - this class can do it, and if it's invoked in this way, it provides an object able to obey the iteration protocol.

# This is why the output of the code is the same as previously, although the object of the Fib class isn't used explicitly inside the for loop's context.


class Fib:
    def __init__(self, nn):
        self.__n = nn
        self.__i = 0
        self.__p1 = self.__p2 = 1

    def __iter__(self):
        print("Fib iter")
        return self

    def __next__(self):
        # print("Fib next")
        self.__i += 1
        if self.__i > self.__n:
            raise StopIteration
        if self.__i in [1, 2]:
            return 1
        ret = self.__p1 + self.__p2
        self.__p1, self.__p2 = self.__p2, ret
        return ret


class Class:
    def __init__(self, n):
        self.__iter = Fib(n)

    def __iter__(self):
        print("Class iter")
        return self.__iter


object = Class(11)

for i in object:
    print(i)
