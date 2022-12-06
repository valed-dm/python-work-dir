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

data = bytearray(10)


# Such an invocation creates a bytearray object able to store ten bytes.

# Note: such a constructor fills the whole array with zeros.

