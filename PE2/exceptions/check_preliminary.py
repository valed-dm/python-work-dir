# How do you handle exceptions? The word try is key to the solution.

# What's more, it's a keyword, too.

# The recipe for success is as follows:

# first, you have to try to do something;
# next, you have to check whether everything went well.
# But wouldn't it be better to check all circumstances first and then do something only if it's safe?

# Just like the example in the editor.

# Admittedly, this way may seem to be the most natural and understandable, but in reality, 
# this method doesn't make programming any easier. 
# All these checks can make your code bloated and illegible.

# Python prefers a completely different approach.

# first_number = int(input("Enter the first number: "))
# second_number = int(input("Enter the second number: "))

# if second_number != 0:
#     print(first_number / second_number)
# else:
#     print("This operation cannot be done.")

# print("THE END.")

# python way:
# the try keyword begins a block of the code which may or may not be performing correctly;
# next, Python tries to perform the risky action; if it fails, an exception is raised 
# and Python starts to look for a solution;
# the except keyword starts a piece of code which will be executed 
# if anything inside the try block goes wrong 
# - if an exception is raised inside a previous try block, 
# it will fail here, so the code located after the except keyword should provide 
# an adequate reaction to the raised exception;
# returning to the previous nesting level ends the try-except section.

# try:
#     :
#     :
# except:
#     :
#     :


# in the first step, Python tries to perform all instructions placed between the try: and except: statements;
# if nothing is wrong with the execution and all instructions are performed successfully, the execution jumps to the point after the last line of the except: block, and the block's execution is considered complete;
# if anything goes wrong inside the try: and except: block, the execution immediately jumps out of the block and into the first instruction located after the except: keyword; this means that some of the instructions from the block may be silently omitted.
# first_number = int(input("Enter the first number: "))
# second_number = int(input("Enter the second number: "))

# try:
#     print(first_number / second_number)
# except:
#     print("This operation cannot be done.")

# print("THE END.")

try:
    print("1")
    x = 1 / 0
    print("2")
except:
    print("Oh dear, something went wrong...")

print("3")
