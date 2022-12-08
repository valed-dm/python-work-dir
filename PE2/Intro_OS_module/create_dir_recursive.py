# Recursive directory creation
# The mkdir function is very useful, but what if you need to create another directory in the directory you've just created. Of course, you can go to the created directory and create another directory inside it, but fortunately the os module provides a function called makedirs, which makes this task easier.

# The makedirs function enables recursive directory creation, which means that all directories in the path will be created. Let's look at the code in the editor and see how it is in practice.

# The code should produce the following result:

# ['my_second_directory']
# output

# The code creates two directories. The first of them is created in the current working directory, while the second in the my_first_directory directory.

# You don't have to go to the my_first_directory directory to create the my_second_directory directory, because the makedirs function does this for you. In the example above, we go to the my_first_directory directory to show that the makedirs command creates the my_second_directory subdirectory.

# To move between directories, you can use a function called chdir, which changes the current working directory to the specified path. As an argument, it takes any relative or absolute path. In our example, we pass the first directory name to it.

# NOTE: The equivalent of the makedirs function on Unix systems is the mkdir command with the -p flag, while in Windows, simply the mkdir command with the path:

# Unix-like systems:

# mkdir -p my_first_directory/my_second_directory

# Windows:

# mkdir my_first_directory/my_second_directory


import os
from os import strerror

try:
    os.makedirs("my_first_directory/my_second_directory")
    os.chdir("my_first_directory")
    print(os.listdir())
except IOError as e:
    print(strerror(e.errno))
    os.chdir("my_first_directory")
    print(os.listdir())

