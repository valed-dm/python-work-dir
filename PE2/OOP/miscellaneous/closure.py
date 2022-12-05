# A brief look at closures
# Let's start with a definition: closure is a technique which allows the storing of values in spite of the fact that the context in which they have been created does not exist anymore. Intricate? A bit.

# Let's analyze a simple example:

def outer(par):
    loc = par


var = 1
outer(var)

print(var)
# print(loc) # loc is not defined


# The example is obviously erroneous.

# The last two lines will cause a NameError exception - neither par nor loc is accessible outside the function. 
# Both the variables exist when and only when the outer() function is being executed.
# Look at the example in the editor. We've modified the code significantly.

def outer(par):
    loc = par

    def inner():
        return loc
    return inner


var = 1
fun_1 = outer(var)
fun_2 = outer(2)
fun_3 = outer(3)
print(fun_1(), fun_2(), fun_3())

print('-------------------')


# There is a brand new element in it - a function (named inner) inside another function (named outer).

# How does it work? Just like any other function except for the fact that inner() may be invoked only from within outer(). We can say that inner() is outer()'s private tool - no other part of the code can access it.

# Look carefully:

# the inner() function returns the value of the variable accessible inside its scope, as inner() can use any of the entities at the disposal of outer()
# the outer() function returns the inner() function itself; more precisely, it returns a copy of the inner() function, the one which was frozen at the moment of outer()'s invocation; the frozen function contains its full environment, including the state of all local variables, which also means that the value of loc is successfully retained, although outer() ceased to exist a long time ago.
# In effect, the code is fully valid, and outputs:

# 1
# output

# The function returned during the outer() invocation is a closure.

# A brief look at closures: continued
# A closure has to be invoked in exactly the same way in which it has been declared.

# In the example below:

def outer(par):
    loc = par

    def inner():
        return loc
    return inner


var = 1
fun = outer(var)
print(fun())

print('-------------------')
# the inner() function is parameterless, so we have to invoke it without arguments.

# Now look at the code in the editor. It is fully possible to declare a closure equipped with an arbitrary number of parameters, e.g., one, just like the power() function.

def make_closure(par):
    loc = par

    def power(p):
        return p ** loc
    return power


fsqr = make_closure(2)
fcub = make_closure(3)

print(fsqr(5))
print(fcub(5))

for i in range(5):
    print(i, fsqr(i), fcub(i))


print('-------------------')

# This means that the closure not only makes use of the frozen environment, but it can also modify its behavior by using values taken from the outside.

# This example shows one more interesting circumstance - you can create as many closures as you want using one and the same piece of code. This is done with a function named make_closure(). Note:

# the first closure obtained from make_closure() defines a tool squaring its argument;
# the second one is designed to cube the argument.
# This is why the code produces the following output:

# 0 0 0
# 1 1 1
# 2 4 8
# 3 9 27
# 4 16 64
# output

# Carry out your own tests.
