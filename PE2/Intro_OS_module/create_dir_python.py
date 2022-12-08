# Creating directories in Python
# The os module provides a function called mkdir, which, like the mkdir command in Unix and Windows, 
# allows you to create a directory. The mkdir function requires a path that can be relative or absolute. 
# Let's recall what both paths look like in practice:

# my_first_directory — this is a relative path which will create the my_first_directory directory in the current working directory;
# ./my_first_directory — this is a relative path that explicitly points to the current working directory. 
# It has the same effect as the path above;
# ../my_first_directory — this is a relative path that will create the my_first_directory directory in the parent directory 
# of the current working directory;
#-------------------------------
# /python/my_first_directory — this is the absolute path!
#-------------------------------
# that will create the my_first_directory directory, which in turn is in the python directory in the root directory.

# Look at the code in the editor. It shows an example of how to create the my_first_directory directory using a relative path. 
# This is the simplest variant of the relative path, which consists of passing only the directory name.

import os
from os import strerror

try:
    os.mkdir("my_first_directory")
    print(sorted(os.listdir()))
except OSError as e:
    print(strerror(e.errno))
    print(('directory content list:\n' + str(sorted(os.listdir()))).strip())

print()
print(sorted(os.listdir('/Users/dmitrijvaledinskij/.android')))
#-------------------------------
# remember realpath cli command
#-------------------------------
# If you test your code here, it will output the newly created ['my_first_directory'] 
# directory (and the entire content of the current working catalog).

# The mkdir function creates a directory in the specified path. 
# Note that running the program twice will raise a FileExistsError.

# This means that we cannot create a directory if it already exists. 
# In addition to the path argument, the mkdir function can optionally take the mode argument, 
# which specifies directory permissions. However, on some systems, the mode argument is ignored.

# To change the directory permissions, we recommend the chmod function, 
# which works similarly to the chmod command on Unix systems. You can find more information about it in the documentation.

# In the above example, another function provided by the os module named listdir is used. 
# The listdir function returns a list containing the names of the files and directories that are in the path passed as an argument.

# If no argument is passed to it, the current working directory will be used (as in the example above). 
# It's important that the result of the listdir function omits the entries '.' and '..', which are displayed, e.g., when using the ls -a command on Unix systems.

# NOTE: In both Windows and Unix, there's a command called mkdir, which requires a directory path. 
# The equivalent of the above code that creates the my_first_directory directory is the mkdir my_first_directory command.
