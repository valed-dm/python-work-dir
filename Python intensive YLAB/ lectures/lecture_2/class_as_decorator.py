# Decorators are a very powerful and useful tool in Python since it allows programmers to modify
# the behaviour of function or class.
# Decorators allow us to wrap another function in order to extend the behaviour of the wrapped function,
# without permanently modifying it.

# We can define a decorator as a class in order to do that,
# we have to use a __call__ method of classes.
# When a user needs to create an object that acts as a function
# then function decorator needs to return an object that acts like a function,
# so __call__ can be useful.
# For Example:
# Python program showing
# use of __call__() method

from time import time


class MyDecorator:
    def __init__(self, function):
        self.function = function

    def __call__(self):

        # We can add some code
        # before function call
        print("-----------------------------------------------")
        print("this is text to be printed before func executes")

        self.function()

        # We can also add some code
        # after function call.
        print("this is text to be printed after func executes")


# adding class decorator to the function
@MyDecorator
def function():
    print("GeeksforGeeks")


function()
print("-----------------------------------------------")


# Class Decorator with *args and **kwargs:

# In order to use class decorator with argument *args and **kwargs
# we used a __call__ function and passed both the argument in a given function:

# Python program showing
# class decorator with *args
# and **kwargs


class MyDecorator:
    def __init__(self, function):
        self.function = function

    def __call__(self, *args, **kwargs):

        # We can add some code
        # before function call
        print("-----------------------------------------------")

        self.function(*args, **kwargs)

        # We can also add some code
        # after function call.
        print("-----------------------------------------------")


# adding class decorator to the function
@MyDecorator
def function(name, message='Hello'):
    print("{}, {}".format(message, name))


function("geeks_for_geeks", "hello")


# Class Decorator with return statement:

# In the given example the functions did not return anything so there is not any issue,
# but one may need the returned value.
# So we use return statement with the class decorator:

# Python program showing
# class decorator with
# return statement

class SquareDecorator:

    def __init__(self, function):
        self.function = function

    def __call__(self, *args, **kwargs):

        # before function
        print("-----------------------------------------------")

        result = self.function(*args, **kwargs)
        self.function(*args, **kwargs)

        # after function
        print("-----------------------------------------------")
        return result


# adding class decorator to the function
@SquareDecorator
def get_square(n):
    print("given number is:", n)
    return n * n


get_square(13)
print("Square of number is:", get_square(195))
print()


# Using class Decorators to print Time required to execute a program:

# In order to print time required to execute a program,
# we use __call__ function and use a time module so that we can get a execute time of a program:

# Python program to execute
# time of a program

# importing time module


class Timer:

    def __init__(self, func):
        self.function = func

    def __call__(self, *args, **kwargs):
        start_time = time()
        result = self.function(*args, **kwargs)
        end_time = time()
        print("Execution took {} seconds".format(end_time-start_time))
        return result


# adding a decorator to the function
@Timer
def some_function(delay):
    from time import sleep

    # Introducing some time delay to simulate a time taking function.
    sleep(delay)


some_function(1)


# Checking error parameter using class decorator:

# This type of class decorator is most frequently used.
# This decorator checks parameters before executing the function preventing the function
# to become overloaded and enables it to store only logical and necessary statements.
# Python program checking
# error parameter using
# class decorator

class ErrorCheck:

    def __init__(self, function):
        self.function = function

    def __call__(self, *params):
        if any([isinstance(i, str) for i in params]):
            raise TypeError("parameter cannot be a string !!!")
        else:
            return self.function(*params)


@ErrorCheck
def add_numbers(*numbers):
    return sum(numbers)


#  returns 6
print(add_numbers(1, 2, 3))

# raises Error.
print(add_numbers(1, '2', 3))
