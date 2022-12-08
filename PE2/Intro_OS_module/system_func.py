# The system() function
# All functions presented in this part of the course can be replaced by a function called system, 
# which executes a command passed to it as a string.

# The system function is available in both Windows and Unix. Depending on the system, 
# it returns a different result.

# In Windows, it returns the value returned by the shell after running the command given, 
# while in Unix, it returns the exit status of the process.

# Let's look at the code in the editor and see how it is in practice.

import os

os.rmdir("my_first_directory")
returned_value = os.system("mkdir my_first_directory")
print('------------------')
print(returned_value)
print('------------------')
print(os.system('ls -a'))

# Result:
# 0
# output

# The above example will work in both Windows and Unix. In our case, we receive exit status 0, 
# which indicates success on Unix systems.

# This means that the my_first_directory directory has been created. As part of the exercise, 
# try to list the contents of the directory where you created the my_first_directory directory.

