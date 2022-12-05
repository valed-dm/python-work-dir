# How to use lambdas and what for?

# The most interesting part of using lambdas appears when you can use them in their pure form -
# as anonymous parts of code intended to evaluate a result.
# Imagine that we need a function (we'll name it print_function) which prints the values of a given 
# (other) function for a set of selected arguments.
# We want print_function to be universal - it should accept a set of arguments 
# put in a list and a function to be evaluated, both as arguments - we don't want to hardcode anything.
# Look at the example in the editor. This is how we've implemented the idea.

def print_function(args, fun):
    for x in args:
        print('f(', x,')=', fun(x), sep='')


def poly(x):
    return 2 * x**2 - 4 * x + 2


print_function([x for x in range(-2, 3)], poly)

print('-------------------')

# Let's analyze it. The print_function() function takes two parameters:

# the first, a list of arguments for which we want to print the results;
# the second, a function which should be invoked as many times as the number of values 
# that are collected inside the first parameter.
# Note: we've also defined a function named poly() - 
# this is the function whose values we're going to print. 
# The calculation the function performs isn't very sophisticated - 
# it's the polynomial (hence its name) of a form:

# f(x) = 2x2 - 4x + 2

# The name of the function is then passed to the print_function() along with a set of five 
# different arguments - the set is built with a list comprehension clause.
# The code prints the following lines:

# f(-2)=18
# f(-1)=8
# f(0)=2
# f(1)=0
# f(2)=2
# output

# Can we avoid defining the poly() function, as we're not going to use it more than once? 
# Yes, we can - this is the benefit a lambda can bring.


# Look at the example below. Can you see the difference?

def print_function(args, fun):
    for x in args:
        print('f(', x,')=', fun(x), sep='')

print_function([x for x in range(-2, 3)], lambda x: 2 * x**2 - 4 * x + 2)

print('-------------------')

# The print_function() has remained exactly the same, but there is no poly() function. 
# We don't need it anymore, as the polynomial is now directly inside the print_function() 
# invocation in the form of a lambda defined in the following way:

lambda x: 2 * x**2 - 4 * x + 2

# The code has become shorter, clearer, and more legible.
# Let us show you another place where lambdas can be useful. 
# We'll start with a description of map(), a built-in Python function. 
# Its name isn't too descriptive, its idea is simple, and the function itself is really usable.

# Lambdas and the map() function

# In the simplest of all possible cases, the map() function:

# ------->>> map(function, list) <<<--------------

# takes two arguments:

# a function;
# a list.
# The above description is extremely simplified, as:

# the second map() argument may be any entity that can be iterated (e.g., a tuple, or just a generator)
# map() can accept more than two arguments.
# The map() function applies the function passed by its first argument to all its second argument's elements,
# and returns an iterator delivering all subsequent function results.

# You can use the resulting iterator in a loop, or convert it into a list using the list() function.

# Can you see a role for any lambda here?

# Look at the code in the editor - we've used two lambdas in it.

print('map function')
list_1 = [x for x in range(5)]
list_2 = list(map(lambda x: 2 ** x, list_1))
print(list_2)

for x in map(lambda x: x * x, list_2):
    print(x, end=' ')

list_3 = list(map(lambda x: x * x, list_2))
print(list_3)

print('-------------------')
# This is the intrigue:

# build the list_1 with values from 0 to 4;
# next, use map along with the first lambda to create a new list in which all elements have been 
# evaluated as 2 raised to the power taken from the corresponding element from list_1;
# list_2 is printed then;
# in the next step, use the map() function again to make use of the generator it returns and
# to directly print all the values it delivers; 
# as you can see, we've engaged the second lambda here - it just squares each element from list_2.
# Try to imagine the same code without lambdas. Would it be any better? It's unlikely.

# Lambdas and the filter() function

# Another Python function which can be significantly beautified by the application of a lambda is filter().
# It expects the same kind of arguments as map(), but does something different - 
# it filters its second argument while being guided by directions flowing from the function 
# specified as the first argument (the function is invoked for each list element, just like in map()).
# The elements which return True from the function pass the filter - the others are rejected.
# The example in the editor shows the filter() function in action.

from random import seed, randint

seed()
data = [randint(-10,10) for x in range(5)]
filtered = list(filter(lambda x: x > 0 and x % 2 == 0, data))

print('filter function')
print(data)
print(filtered)


# Note: we've made use of the random module to initialize the random number generator 
# (not to be confused with the generators we've just talked about) with the seed() function, 
# and to produce five random integer values from -10 to 10 using the randint() function.
# The list is then filtered, and only the numbers which are even and greater than zero are accepted.
# Of course, it's not likely that you'll receive the same results, but this is what our results looked like:
# [6, 3, 3, 2, -7]
# [6, 2]