def scope_test():
    x = 123

scope_test()
# print(x)

# def my_function():
#     var = 2
#     print("Do I know that variable?", var)

# var = 1
# my_function()
# print(var)

# the var variable created inside the function is not the same as when defined outside it - it seems that there two different variables of the same name;
# moreover, the function's variable shadows the variable coming from the outside world.
# It also means that the scope of a variable existing outside a function is supported only when getting its value (reading). Assigning a value forces the creation of the function's own variable.

def my_function():
    global var
    var = 2
    print("Do I know that variable?", var)


var = 1
my_function()
print(var)


# global name
# global name1, name2, ...
# Using this keyword inside a function with the name (or names separated with commas) of a variable(s), forces Python to refrain from creating a new variable inside the function - the one accessible from outside will be used instead.
# In other words, this name becomes global (it has a global scope, and it doesn't matter whether it's the subject of read or assign).