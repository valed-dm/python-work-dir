# A Python generator is a piece of specialized code able to produce a series of values, and to control the iteration process. This is why generators are very often called iterators, and although some may find a very subtle distinction between these two, we'll treat them as one.

# You may not realize it, but you've encountered generators many, many times before. Take a look at the very simple snippet:

for i in range(5):
    print(i)


# The range() function is, in fact, a generator, which is (in fact, again) an iterator.

# What is the difference?

# A function returns one, well-defined value - it may be the result of a more or less complex evaluation of, e.g., a polynomial, and is invoked once - only once.

# A generator returns a series of values, and in general, is (implicitly) invoked more than once.

# In the example, the range() generator is invoked six times, providing five subsequent values from zero to four, and finally signaling that the series is complete.

# The above process is completely transparent. Let's shed some light on it. Let's show you the iterator protocol.

