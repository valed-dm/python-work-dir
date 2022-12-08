import os
print(os.uname())

# Getting information about the operating system
# Before you create your first directory structure, you'll see how you can get information about the current operating system. 
# This is really easy because the os module provides a function called uname, which returns an object containing the following attributes:

# systemname — stores the name of the operating system;
# nodename — stores the machine name on the network;
# release — stores the operating system release;
# version — stores the operating system version;
# machine — stores the hardware identifier, e.g., x86_64.

# As you can see, the uname function returns an object containing information about the operating system. 
# The above code was launched on Ubuntu 16.04.6 LTS, so don't be surprised if you get a different result, 
# because it depends on your operating system.

# Unfortunately, the uname function only works on some Unix systems. 
# If you use Windows, you can use the uname function in the platform module, which returns a similar result.

# The os module allows you to quickly distinguish the operating system using the name attribute, 
# which supports one of the following names:

# posix — you'll get this name if you use Unix;
# nt — you'll get this name if you use Windows;
# java — you'll get this name if your code is written in Jython.
# For Ubuntu 16.04.6 LTS, the name attribute returns the name posix:


print('------------------')


import os
print(os.name)


# Result:

# posix
# output

# NOTE: On Unix systems, there's a command called uname that returns the same information (if you run it with the -a option) as the uname function.

