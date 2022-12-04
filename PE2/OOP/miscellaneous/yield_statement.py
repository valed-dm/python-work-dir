# The yield statement
# The iterator protocol isn't particularly difficult to understand and use, but it is also indisputable that the protocol is rather inconvenient.

# The main discomfort it brings is the need to save the state of the iteration between subsequent __iter__ invocations.

# For example, the Fib iterator is forced to precisely store the place in which the last invocation has been stopped (i.e., the evaluated number and the values of the two previous elements). This makes the code larger and less comprehensible.

# This is why Python offers a much more effective, convenient, and elegant way of writing iterators.

# The concept is fundamentally based on a very specific and powerful mechanism provided by the yield keyword.

# You may think of the yield keyword as a smarter sibling of the return statement, with one essential difference.

# Take a look at this function:

def fun(n):
    for i in range(n):
        return i


# It looks strange, doesn't it? It's clear that the for loop has no chance to finish its first execution, as the return will break it irrevocably.

# Moreover, invoking the function won't change anything - the for loop will start from scratch and will be broken immediately.

# We can say that such a function is not able to save and restore its state between subsequent invocations.

# This also means that a function like this cannot be used as a generator.




# We've replaced exactly one word in the code - can you see it?

def fun(n):
    for i in range(n):
        yield i


# We've added yield instead of return. This little amendment turns the function into a generator, and executing the yield statement has some very interesting effects.

# First of all, it provides the value of the expression specified after the yield keyword, just like return, but doesn't lose the state of the function.

# All the variables' values are frozen, and wait for the next invocation, when the execution is resumed (not taken from scratch, like after return).

# There is one important limitation: such a function should not be invoked explicitly as - in fact - it isn't a function anymore; it's a generator object.

# The invocation will return the object's identifier, not the series we expect from the generator.

# Due to the same reasons, the previous function (the one with the return statement) may only be invoked explicitly, and must not be used as a generator.

# How to build a generator
# Let us show you the new generator in action.

# This is how we can use it:

def fun(n):
    for i in range(n):
        yield i


print(fun(10))

for v in fun(5):
    print(v)


# Can you guess the output?
