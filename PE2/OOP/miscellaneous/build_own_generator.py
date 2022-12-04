# What if you need a generator to produce the first n powers of 2?
# Nothing easier. Just look at the code below:

def powers_of_2(n):
    power = 1
    for i in range(n):
        yield power
        power *= 2


for v in powers_of_2(8):
    print(v)

print()

# List comprehensions
# Generators may also be used within list comprehensions, just like here:


def powers_of_2(n):
    power = 1
    for i in range(n):
        yield power
        power *= 2


t = [(x + 100)/4 for x in powers_of_2(10)]
print(t)

print()

# The list() function
# The list() function can transform a series of subsequent generator invocations into a real list:


def powers_of_2(n):
    power = 1
    for i in range(n):
        yield power
        power *= 2


t = list(powers_of_2(10))
print(t)

print()

# The in operator
# Moreover, the context created by the in operator allows you to use a generator, too.
# The example shows how to do it:


def powers_of_2(n):
    power = 1
    for i in range(n):
        yield power
        power *= 2


for i in range(20):
    if i in powers_of_2(4):
        print(i)

print()

# The Fibanacci number generator
# Now let's see a Fibonacci number generator, and ensure that it looks much better than the objective version based on the direct iterator protocol implementation.
# Here it is:


def fibonacci(n):
    p = pp = 1
    for i in range(n):
        if i in [0, 1]:
            yield 1
        else:
            n = p + pp
            pp, p = p, n
            yield n


fibs = list(fibonacci(10))
print(fibs)
