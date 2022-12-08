# Deleting directories in Python
# The os module also allows you to delete directories. It gives you the option of deleting a single directory 
# or a directory with its subdirectories. To delete a single directory, you can use a function called rmdir, 
# which takes the path as its argument. Look at the code in the editor.

# The above example is really simple. First, the my_first_directory directory is created, 
# and then it's removed using the rmdir function. The listdir function is used as proof that the directory 
# has been removed successfully. In this case, it returns an empty list. 
# When deleting a directory, make sure it exists and is empty, otherwise an exception will be raised.

# To remove a directory and its subdirectories, you can use the removedirs function, 
# which requires you to specify a path containing all directories that should be removed:

import os

os.mkdir("my_first_directory")
print(sorted(os.listdir()))
os.rmdir("my_first_directory")
print(sorted(os.listdir()))

os.makedirs("my_first_directory/my_second_directory")


print(sorted(os.listdir()))
print('---------------------------')
os.removedirs("my_first_directory/my_second_directory")
print(sorted(os.listdir()))


# As with the rmdir function, if one of the directories doesn't exist or isn't empty, an exception will be raised.

# NOTE: In both Windows and Unix, there's a command called rmdir, which, just like the rmdir function, 
# removes directories. What's more, both systems have commands to delete a directory and its contents. 
# In Unix, this is the rm command with the -r flag.