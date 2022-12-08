# Where am I now?
# You already know how to create directories and how to move between them. Sometimes, when you have a really large directory structure that you navigate, you may not know which directory you're currently working in.


# As you’ve probably guessed, the os module provides a function that returns information about the current working directory. It's called getcwd. Look at the code in the editor to see how to use it in practice.

# Result:

# .../my_first_directory
# .../my_first_directory/my_second_directory
# output

# In the example, we create the my_first_directory directory, and the my_second_directory directory inside it. In the next step, we change the current working directory to the my_first_directory directory, and then display the current working directory (first line of the result).

# Next, we go to the my_second_directory directory and again display the current working directory (second line of the result). As you can see, the getcwd function returns the absolute path to the directories.

# NOTE: On Unix-like systems, the equivalent of the getcwd function
#--------------------------------
# is the pwd command, which prints the name of the current working directory.
# pwd
# realpath
#--------------------------------


import os
from os import strerror

try:
    os.makedirs("my_first_directory/my_second_directory")
    os.chdir("my_first_directory")
    print(os.getcwd())
    os.chdir("my_second_directory")
    print(os.getcwd())
except OSError as e:
    print(strerror(e.errno))
    os.chdir("my_first_directory")
    print(os.getcwd())
    os.chdir("my_second_directory")
    print(os.getcwd())
