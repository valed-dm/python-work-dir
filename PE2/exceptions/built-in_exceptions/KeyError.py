# Location: BaseException ← Exception ← LookupError ← KeyError

# Description: a concrete exception raised when you try to access a collection's non-existent element (e.g., a dictionary's element)

# How to abuse the dictionary
# and how to deal with it?

dictionary = { 'a': 'b', 'b': 'c', 'c': 'd' }
ch = 'a'

try:
    while True:
        ch = dictionary[ch]
        print(ch)
except KeyError:
    print('No such key:', ch)


# We are done with exceptions for now, but they'll return when we discuss 
# object-oriented programming in Python. 
# You can use them to protect your code from bad accidents, 
# but you also have to learn how to dive into them, exploring the information they carry.

# Exceptions are in fact objects - however, we can tell you nothing about 
# this aspect until we present you with classes, objects, and the like.

# For the time being, if you'd like to learn more about exceptions on your own, 
# you look into Standard Python Library at https://docs.python.org/3.6/library/exceptions.html.