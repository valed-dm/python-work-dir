from platform import platform
print(platform())
print(platform(1))
print(platform(0, 1))


# This is how you can invoke it:

# platform(aliased = False, terse = False)
# And now:

# aliased → when set to True (or any non-zero value) it may cause the function to present the alternative underlying layer names instead of the common ones;
# terse → when set to True (or any non-zero value) it may convince the function to present a briefer form of the result (if possible)

# The machine function
# Sometimes, you may just want to know the generic name of the processor which runs your OS together with Python and your code - a function named machine() will tell you that. As previously, the function returns a string.

from platform import machine
print(machine())

# The processor function
# The processor() function returns a string filled with the real processor name (if possible).

from platform import processor
print(processor())

# The system function
# A function named system() returns the generic OS name as a string.

from platform import system
print(system())

# The version function
# The OS version is provided as a string by the version() function.

from platform import version
print(version())

# macOS-12.6-x86_64-i386-64bit
# macOS-12.6-x86_64-i386-64bit
# macOS-12.6
# x86_64
# i386
# Darwin
# Darwin Kernel Version 21.6.0: Mon Aug 22 20:17:10 PDT 2022; root:xnu-8020.140.49~2/RELEASE_X86_64

# The python_implementation and the python_version_tuple functions

# If you need to know what version of Python is running your code, you can check it using a number of dedicated functions - here are two of them:

# python_implementation() → returns a string denoting the Python implementation (expect CPython here, unless you decide to use any non-canonical Python branch)

# python_version_tuple() → returns a three-element tuple filled with:
# the major part of Python's version;
# the minor part;
# the patch level number.

from platform import python_implementation, python_version_tuple

print(python_implementation())

for atr in python_version_tuple():
    print(atr)