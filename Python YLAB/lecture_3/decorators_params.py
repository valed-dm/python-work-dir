# https://www.geeksforgeeks.org/decorators-with-parameters-in-python/

# Decorators with parameters is similar to normal decorators.


# The syntax for decorators with parameters:

#       -------------------------------------------
#       @decorator(params)
#       def func_name():
#           ''' Function implementation'''
#       -------------------------------------------

# The above code is equivalent to:

#       -------------------------------------------
#       def func_name():
#           ''' Function implementation'''

#       func_name = (decorator(params))(func_name)
#
# As the execution starts from left to right:
#       --> decorator(params) is called
#       --> a function object fun_obj is returned.
#       --> Using the fun_obj the call fun_obj(func_name) is made.
#       --> Inside the inner function, required operations are performed;
#       --> The actual function reference is returned which will be assigned to func_name.
# Now, func_name() can be used to call the function with decorator applied on it.

# -------------------------------------------
# How Decorator with parameters is implemented:
# Here params can also be empty.

params = {}


def decorators(*args, **kwargs):
    def inner(func):
        '''
           do operations with func
        '''
        return func
    return inner  # this is the fun_obj mentioned in the above content


@decorators(params)
def func():
    """
         function implementation
    """
# -------------------------------------------

# Observe these first :
# Python code to illustrate Decorators basic in Python


def decorator_fun(func):
    print("Inside decorator 1")

    def inner(*args, **kwargs):
        print("Inside inner function 1")
        print("Decorated the function 1")
        # do operations with func
        func()
    return inner #inner()


@decorator_fun
def func_to():
    print("Inside actual function 1")

func_to()


print(40*"-")
# -------------------------------------------
# Another Way:
# Python code to illustrate Decorators with parameters in Python


def decorator_fun(func):
    print("Inside decorator 2")

    def inner(*args, **kwargs):
        print("Inside inner function 2")
        print("Decorated the function 2")

        func()

    return inner


def func_to():
    print("Inside actual function 2")


# another way of using decorators
decorator_fun(func_to)()

print(40*"-")
# -------------------------------------------
# Example #1
# Python code to illustrate Decorators with parameters in Python:


def decorator(*args, **kwargs):
    print("Inside decorator 3")

    def inner(func):

        # code functionality here
        print("Inside wrapper function 3")
        print("I like", kwargs['like'])

        func()

    # returning inner function
    return inner


@decorator(like="geeksforgeeks")
def my_func():
    print("Inside actual function 3")

print(40*"-")

# -------------------------------------------
# Example #2
# Python code to illustrate Decorators with parameters in Python:
# This example also tells us that Outer function parameters can be accessed by the enclosed inner function.


def decorator_func(x, y):

    def inner(func):

        def wrapper(*args, **kwargs):
            print("I like Geeksforgeeks")
            print("Summation of values - {}".format(x+y))

            func(*args, **kwargs)

        return wrapper

    return inner


# Not using decorator
def my_fun(*args):
    for ele in args:
        print(ele)


# another way of using decorators
decorator_func(12, 15)(my_fun)('Geeks', 'for', 'Geeks')


print(40*"-")

# -------------------------------------------
# Example #3
# Python code to illustrate Decorators with parameters in Python:


def decodecorator(dataType, message1, message2):
    def decorator(fun):
        print(message1)

        def wrapper(*args, **kwargs):
            print(message2)
            if all([type(arg) == dataType for arg in args]):
                return fun(*args, **kwargs)
            return "Invalid Input"
        return wrapper
    return decorator


@decodecorator(str, "Decorator for 'stringJoin'", "stringJoin started ...")
def stringJoin(*args):
    st = ''
    for i in args:
        st += i
    return st


@decodecorator(int, "Decorator for 'summation'\n", "summation started ...")
def summation(*args):
    summ = 0
    for arg in args:
        summ += arg
    return summ


print(stringJoin("I ", 'like ', "Geeks", 'for', "geeks"))
print()
print(summation(19, 2, 8, 533, 67, 981, 119))
# -------------------------------------------
