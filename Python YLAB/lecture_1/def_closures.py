def newfunc(n):
    def myfunc(x):
        return x + n
    return myfunc


new_0 = newfunc(100)
new_1 = newfunc(200)
new_2 = newfunc(300)

print(new_0(200))
print(new_1(200))
print(new_2(200))

print("---------------------- nonlocal variables in python ----------------------")
# Nonlocal variables in Python
# Variables that are defined in the enclosing function, but not in the nested function
# are known as Nonlocal variables. A nested function can access any nonlocal variable of its enclosing function.

# In this code example, the function func2() is the Nested function
# and the function func1() is called the Enclosed function.

# By default, a nested function can’t modify nonlocal variables.


def func1():            # Enclosed function
    var = "PythonGeeks"  # Nonlocal variable

    def func2():        # Nested function
        print(var)
    func2()


func1() # prints PythonGeeks


def func1():

    var = "Enclosed Function"

    def func2():
        var = "Nested Function"
        print("print from nested func:", var)

    func2()
    print("print from enclosed func:", var)


func1()

# We must use the keyword nonlocal and declare the variable in the nested function
#  to modify a nonlocal variable from a nested function.


def func1():
    var = "Enclosed Function"

    def func2():
        nonlocal var
        var = "Nested Function"
        print(var)
    func2()
    print(var)


func1()

# In the above code example, the nested function func2() modified the variable var
# which is in the scope of enclosed function func1().


# Closure in Python
# To understand the concept of closure, let us first define a closure function.
# To define a closure function, we need to first define a nested function
# that reads one or more nonlocal variables and finally return the nested function.

# Example of a closure function in Python
print("---------------------- closure function ----------------------")
def forest():
    animals = 200

    def population():
        return animals

    return population


amazon = forest()
del forest
print(amazon())

# In the above code example, even after we deleted the enclosed function,
# the nested function still accessed the values of nonlocal variables and ran without raising any errors.

# This happens because Python creates an environment for the nested function by connecting
# the values of nonlocal variables to the nested function.

# This method of remembering the values of nonlocal variables even if the variables are no longer in scope
# or the function is no longer in the current namespace is called Closure.


# Requirements of Python closure function:

# We must meet the following requirements to create a closure function.

# 1. Define a nested function
# 2. Return the Nested function
# 3. The Nested function should access a nonlocal variable.


# Advantages of closure in Python

# The following are some of the well-known benefits of closure in Python:

# 1. Avoid the usage of global variables
# 2. Makes code look elegant
# 3. Data hiding
# 4. Preferred more than classes when working with a few number of functions.
# 5. Rather than implementing classes, implementing closure is more efficient.

# Uses of Closure in Python
# One of the most common applications of closure in Python is decorators.
# The core principle of the decorator is based on closure.


# Example of closure in Python
# example of decorator in Python:


def math(func):  # decorator
    def div(numerator, denominator):
        if denominator == 0:
            return "Zero Division Error"
        return func(numerator, denominator)
    return div


@math  # decorator
def division(a, b):  # this function is passed to the math function!
    return a/b


print('---------------------- decorator func output ----------------------')
print(division(4, 2))
print(division(4, 0))


# Python Interview Questions on Closure in Python

# Q1. Define a nested function student() within the function school().
# Define a nonlocal variable day=”Sunday” and use the nested function to print that variable.
# Ans 1. Complete code is as follows:

print('---------------------- questions ----------------------')


def school():
    day = "Sunday"

    def student():
        print(day)
    student()


print("Q1", end=" --> ")
school()  # Output --> Sunday


# Q2. Define a function create_powers(X) which returns a function power(Y) which returns YX.
# Ans 2. Complete code is as follows:

def create_powers(num):
    def power(n):
        return pow(n, num)
    return power


print("Q2, create_powers", end=" --> ")
cube = create_powers(3)
print(cube(2), end=", ")
square = create_powers(2)
print(square(2))
# Output
# 8
# 4


# Q3. What is the output of the below code?

def func1():
    var1 = "Python"

    def func2():
        var2 = "Geeks"
        return var1+var2
    return func2


func3 = func1()
print("Q3", end=" --> ")
print(func3())

# Ans 3. The output of the given code is:
# PythonGeeks


# Q4. Does the below code raise any error.
# If not, then what is the output of the below code?

def city():
    men = 50000
    women = 48000
    children = 25000

    def get_total():
        return men+women+children
    return get_total


population = city()

del city

print("Q4", end=" --> ")
print(population())

# Ans 4. The given code doesn’t raise any errors and its output is:
# 123000

# Q5. Show an application of closure in Python.
# Ans 5. The most common application of closure is decorators in Python.


# Conclusion

# In this article, we learned about closure in Python.
# See how to create a closure function and its benefits.
# Then learn about the most common application of closure in Python.
# Additionally, please feel free to post any queries in the comments section.
