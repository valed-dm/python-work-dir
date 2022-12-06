# How to read bytes from a stream
# An alternative way of reading the contents of a binary file is offered by the method named read().

# Invoked without arguments, it tries to read all the contents of the file into the memory, 
# making them a part of a newly created object of the bytes class.

# This class has some similarities to bytearray, with the exception of one significant difference - 
# it's immutable.

# Fortunately, there are no obstacles to creating a byte array by taking its initial value 
# directly from the bytes object, just like here:

from os import strerror

try:
    bf = open('/Users/dmitrijvaledinskij/Python/data/file.bin', 'rb')
    data = bytearray(bf.read())
    bf.close()

    for b in data:
        print(hex(b), end=' ')

except IOError as e:
    print("I/O error occurred:", strerror(e.errno))


# Be careful - don't use this kind of read if you're not sure that the file's contents 
# will fit the available memory.