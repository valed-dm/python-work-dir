# Special Symbols Used for passing arguments:

# *args (Non-Keyword Arguments)
# **kwargs (Keyword Arguments)

# “We use the “wildcard” or “*” notation like this – *args OR **kwargs – as our function’s argument
# when we have doubts about the number of  arguments we should pass in a function.”

# ----------------------------------------------------------------
# Python program to illustrate *args for a variable number of arguments:
def myFun(*argv):
    for arg in argv:
        print(arg)


myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')
print()

# ----------------------------------------------------------------

# Python program to illustrate *args with a first extra argument:


def myFun(arg1, *argv):
    print("First argument :", arg1)
    for arg in argv:
        print("Next argument through *argv :", arg)


myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')
print()
# ----------------------------------------------------------------
# Python program to illustrate *kwargs for a variable number of keyword arguments:

# Here **kwargs accept keyworded variable-length argument passed by the function call.
# For first=’Geeks’ first is key and ‘Geeks’ is a value. In simple words, what we assign is value,
# and to whom we assign is key.


def myFun(**kwargs):
    for key, value in kwargs.items():
        print("%s == %s" % (key, value))
        print((key, value))


myFun(first='Geeks', mid='for', last='Geeks')
print()

# ----------------------------------------------------------------
# Python program to illustrate  **kwargs for a variable number of keyword arguments
# with one extra argument:

# All the same, but one change is we passing non-keyword argument which acceptable by
# positional argument(arg1 in myFun), and keyword arguments we passing are acceptable by **kwargs.


def myFun(arg1, **kwargs):
    print(arg1)
    for key, value in kwargs.items():
        print(arg1)
        print("%s == %s" % (key, value))


myFun("Hi", first='Geeks', mid='for', last='Geeks')
print()


# ----------------------------------------------------------------
# Using both *args and **kwargs to call a function

# Here, we are passing *args and **kwargs as an argument in the myFun function.
# By passing *args to myFun simply means that we pass the positional and variable-length arguments
# which are contained by args. so, “Geeks” pass to the arg1 , “for” pass to the arg2, and “Geeks” pass to the arg3.
#
# When we pass **kwargs as an argument to the myFun it means that it accepts keyword arguments.
# Here, “arg1” is key and the value is “Geeks” which is passed to arg1,
# and just like that “for” and “Geeks” pass to arg2 and arg3 respectively.
# After passing all the data we are printing all the data in lines.

def myFun(arg1, arg2, arg3):
    print("arg1:", arg1)
    print("arg2:", arg2)
    print("arg3:", arg3)


# Now we can use *args or **kwargs to
# pass arguments to this function :
args = ("Geeks", "for", "Geeks")
myFun(*args)
print()

kwargs = {"arg1": "Geeks", "arg2": "for", "arg3": "Geeks"}
myFun(**kwargs)
print()


# Here, we are passing *args and **kwargs as an argument in the myFun function.
# Where ‘geeks’, ‘for’, ‘geeks’ is passed as *args, and first=”Geeks”, mid=”for”, last=”Geeks”
# is passed as **kwargs and printing in the same line.

def myFun(*args, **kwargs):
    print("args: ", args)
    print("kwargs: ", kwargs)


# Now we can use both *args ,**kwargs
# to pass arguments to this function :
myFun('geeks', 'for', 'geeks', first="Geeks", mid="for", last="Geeks")
print()


# ----------------------------------------------------------------
# Using *args and **kwargs to set values of object

# --> *args receives arguments as a tuple.
# --> **kwargs receives arguments as a dictionary.

class car():  # defining car class
    def __init__(self, *args):  # args receives unlimited no. of arguments as an array
        self.speed = args[0]  # access args index like array does
        self.color = args[1]

# creating objects of car class


audi = car(200, 'red')
bmw = car(250, 'black')
mb = car(190, 'white')

print(audi.color)
print(bmw.speed)
print()

# With **kwargs:
class car(): #defining car class
    def __init__(self,**kwargs): #args receives unlimited no. of arguments as an array
        self.speed = kwargs['s'] #access args index like array does
        self.color = kwargs['c']
                 
#creating objects of car class
         
audi=car(s=200,c='red')
bmw=car(s=250,c='black')
mb=car(s=190,c='white')
    
print(audi.color)
print(bmw.speed)
