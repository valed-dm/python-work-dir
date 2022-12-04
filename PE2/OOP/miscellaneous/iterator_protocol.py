# The iterator protocol is a way in which an object should behave to conform to the rules imposed by the context of the for and in statements. An object conforming to the iterator protocol is called an iterator.

# An iterator must provide two methods:

# __iter__() which should return the object itself and which is invoked once (it's needed for Python to successfully start the iteration)
# __next__() which is intended to return the next value (first, second, and so on) of the desired series - it will be invoked by the for/in statements in order to pass through the next iteration; if there are no more values to provide, the method should raise the StopIteration exception.
# Does it sound strange? Not at all. Look at the example in the editor.

# We've built a class able to iterate through the first n values (where n is a constructor parameter) of the Fibonacci numbers.

# Let us remind you - the Fibonacci numbers (Fibi) are defined as follows:

# Fib1 = 1
# Fib2 = 1
# Fibi = Fibi-1 + Fibi-2

# In other words:

# the first two Fibonacci numbers are equal to 1;
# any other Fibonacci number is the sum of the two previous ones (e.g., Fib3 = 2, Fib4 = 3, Fib5 = 5, and so on)
# Let's dive into the code:

# lines 2 through 6: the class constructor prints a message (we'll use this to trace the class's behavior), prepares some variables (__n to store the series limit, __i to track the current Fibonacci number to provide, and __p1 along with __p2 to save the two previous numbers);

# lines 8 through 10: the __iter__ method is obliged to return the iterator object itself; its purpose may be a bit ambiguous here, but there's no mystery; try to imagine an object which is not an iterator (e.g., it's a collection of some entities), but one of its components is an iterator able to scan the collection; the __iter__ method should extract the iterator and entrust it with the execution of the iteration protocol; as you can see, the method starts its action by printing a message;

# lines 12 through 21: the __next__ method is responsible for creating the sequence; it's somewhat wordy, but this should make it more readable; first, it prints a message, then it updates the number of desired values, and if it reaches the end of the sequence, the method breaks the iteration by raising the StopIteration exception; the rest of the code is simple, and it precisely reflects the definition we showed you earlier;

# lines 24 and 25 make use of the iterator.

# The code produces the following output:

# __init__
# __iter__
# __next__
# 1
# __next__
# 1
# __next__
# 2
# __next__
# 3
# __next__
# 5
# __next__
# 8
# __next__
# 13
# __next__
# 21
# __next__
# 34
# __next__
# 55
# __next__
# output

# Look:

# the iterator object is instantiated first;
# next, Python invokes the __iter__ method to get access to the actual iterator;
# the __next__ method is invoked eleven times - the first ten times produce useful values, while the eleventh terminates the iteration.

class Fib:
    def __init__(self, nn):
        print("__init__")
        self.__n = nn
        self.__i = 0
        self.__p1 = self.__p2 = 1

    def __iter__(self):
        print("__iter__")
        return self

    def __next__(self):
        print("__next__")
        self.__i += 1
        if self.__i > self.__n:
            raise StopIteration
        if self.__i in [1, 2]:
            return 1
        ret = self.__p1 + self.__p2
        self.__p1, self.__p2 = self.__p2, ret
        return ret


for i in Fib(11):
    print(i)
