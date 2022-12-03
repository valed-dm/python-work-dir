# The BaseException class introduces a property named args.
# It's a tuple designed to gather all arguments passed to the class constructor.
# It is empty if the construct has been invoked without any arguments,
# or contains just one element when the constructor gets one argument (we don't count the self argument here), and so on.

# We've prepared a simple function to print the args property in an elegant way. You can see the function in the editor.


def print_args(args):
    lng = len(args)
    if lng == 0:
        print("")
    elif lng == 1:
        print(args[0])
    else:
        print(str(args))


try:
    raise Exception
except Exception as e:
    print(e, e.__str__(), sep=' : ', end=' : ')
    print_args(e.args)

try:
    raise Exception("my exception")
except Exception as e:
    print(e, e.__str__(), sep=' : ', end=' : ')
    print_args(e.args)

try:
    raise Exception("my", "exception")
except Exception as e:
    print(e, e.__str__(), sep=' : ', end=' : ')
    print_args(e.args)
    

# We've used the function to print the contents of the args property in three different cases,
# where the exception of the Exception class is raised in three different ways.
# To make it more spectacular, we've also printed the object itself, along with the result of the __str__() invocation.

# The first case looks routine - there is just the name Exception after the raise keyword.
# This means that the object of this class has been created in a most routine way.

# The second and third cases may look a bit weird at first glance,
# but there's nothing odd here - these are just the constructor invocations.
# In the second raise statement, the constructor is invoked with one argument, and in the third, with two.

# As you can see, the program output reflects this, showing the appropriate contents of the args property:

#  :  :
# my exception : my exception : my exception
# ('my', 'exception') : ('my', 'exception') : ('my', 'exception')
