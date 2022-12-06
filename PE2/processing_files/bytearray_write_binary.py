# Bytearrays: continued
# So, how do we write a byte array to a binary file?

# Look at the code in the editor. Let's analyze it:

from os import strerror

data = bytearray(10)

for i in range(len(data)):
    data[i] = 10 + i

try:
    bf = open('/Users/dmitrijvaledinskij/Python/data/file.bin', 'wb') # bf = binary file
    bf.write(data)
    bf.close()
except IOError as e:
    print("I/O error occurred:", strerror(e.errno))


# Your code that reads bytes from the stream should go here.

# first, we initialize bytearray with subsequent values starting from 10; if you want the file's contents to be clearly readable, replace 10 with something like ord('a') - this will produce bytes containing values corresponding to the alphabetical part of the ASCII code (don't think it will make the file a text file - it's still binary, as it was created with a wb flag);
# then, we create the file using the open() function - the only difference compared to the previous variants is the open mode containing the b flag;
# the write() method takes its argument (bytearray) and sends it (as a whole) to the file;
# the stream is then closed in a routine way.
# The write() method returns a number of successfully written bytes.

# If the values differ from the length of the method's arguments, it may announce some write errors.

# In this case, we haven't made use of the result - this may not be appropriate in every case.

# Try to run the code and analyze the contents of the newly created output file.

# You're going to use it in the next step.


# How to read bytes from a stream
# Reading from a binary file requires use of a specialized method name readinto(), 
# as the method doesn't create a new byte array object, 
# but fills a previously created one with the values taken from the binary file.

# Note:

# the method returns the number of successfully read bytes;
# the method tries to fill the whole space available inside its argument; 
# if there are more data in the file than space in the argument, 
# the read operation will stop before the end of the file; 
# otherwise, the method's result may indicate that the byte array has only been filled 
# fragmentarily (the result will show you that, too, and the part of the array not being used 
# by the newly read contents remains untouched)
# Look at the complete code below:


data = bytearray(10)

try:
    bf = open('/Users/dmitrijvaledinskij/Python/data/file.bin', 'rb')
    bf.readinto(data)
    bf.close()

    for b in data:
        print(hex(b), end=' ')
except IOError as e:
    print("I/O error occurred:", strerror(e.errno))


# Let's analyze it:

# first, we open the file (the one you created using the previous code) with the mode described as rb;
# then, we read its contents into the byte array named data, of size ten bytes;
# finally, we print the byte array contents - are they the same as you expected?
# Run the code and check if it's working.
