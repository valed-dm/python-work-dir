# How to read bytes from a stream: continued
# If the read() method is invoked with an argument, 
# it specifies the maximum number of bytes to be read.

# The method tries to read the desired number of bytes from the file, 
# and the length of the returned object can be used to determine the number of bytes actually read.

# You can use the method just like here:


from os import strerror

try:
    bf = open('/Users/dmitrijvaledinskij/Python/data/file.bin', 'rb')
    data = bytearray(bf.read(5))
    bf.close()

    for b in data:
        print(hex(b), end=' ')

except IOError as e:
    print("I/O error occurred:", strerror(e.errno))


# Note: the first five bytes of the file have been read by the code - 
# the next five are still waiting to be processed.
