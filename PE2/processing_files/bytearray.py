# What is a bytearray?
# Before we start talking about binary files, we have to tell you about one of the specialized classes Python uses to store amorphous data.

# Amorphous data is data which have no specific shape or form - they are just a series of bytes.

# This doesn't mean that these bytes cannot have their own meaning, or cannot represent any useful object,
# e.g., bitmap graphics.

# The most important aspect of this is that in the place where we have contact with the data,
# we are not able to, or simply don't want to, know anything about it.

# Amorphous data cannot be stored using any of the previously presented means -
# they are neither strings nor lists.

# There should be a special container able to handle such data.


# Python has more than one such container - one of them is a specialized class name bytearray -
# as the name suggests, it's an array containing (amorphous) bytes.

# If you want to have such a container, e.g., in order to read in a bitmap image and process it in any way,
# you need to create it explicitly, using one of available constructors.

# Take a look:

# data = bytearray(10)


# Such an invocation creates a bytearray object able to store ten bytes.

# Note: such a constructor fills the whole array with zeros.


# Bytearrays: continued
# Bytearrays resemble lists in many respects. For example, they are mutable, they're a subject of the
# len() function, and you can access any of their elements using conventional indexing.

# There is one important limitation - you mustn't set any byte array elements with a value which is not
# an integer (violating this rule will cause a TypeError exception) and you're not allowed to assign
# a value that doesn't come from the range 0 to 255 inclusive
# (unless you want to provoke a ValueError exception).

# You can treat any byte array elements as integer values - just like in the example in the editor.

# Note: we've used two methods to iterate the byte arrays, and made use of the hex() function
# to see the elements printed as hexadecimal values.

# Now we're going to show you how to write a byte array to a binary file - binary,
# as we don't want to save its readable representation -
# we want to write a one-to-one copy of the physical memory content, byte by byte.

data = bytearray(10)

for i in range(len(data)):
    data[i] = 10 - i

for b in data:
    print(hex(b))
    print(b)

# print(2**8)