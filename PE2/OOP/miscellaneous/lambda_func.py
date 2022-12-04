# The lambda function
# The lambda function is a concept borrowed from mathematics, more specifically, from a part called the Lambda calculus, but these two phenomena are not the same.

# Mathematicians use the Lambda calculus in many formal systems connected with logic, recursion, or theorem provability. Programmers use the lambda function to simplify the code, to make it clearer and easier to understand.

# A lambda function is a function without a name (you can also call it an anonymous function). Of course, such a statement immediately raises the question: how do you use anything that cannot be identified?

# Fortunately, it's not a problem, as you can name such a function if you really need, but, in fact, in many cases the lambda function can exist and work while remaining fully incognito.

# The declaration of the lambda function doesn't resemble a normal function declaration in any way - see for yourself:

# --->>> lambda parameters: expression <<<----


# Such a clause returns the value of the expression when taking into account the current value of the current lambda argument.

# As usual, an example will be helpful. Our example uses three lambda functions, but gives them names. Look at it carefully:

two = lambda: 2
sqr = lambda x: x * x
pwr = lambda x, y: x ** y

for a in range(-2, 3):
    print(sqr(a), end=" ")
    print(pwr(a, two()))


# Let's analzye it:
# the first lambda is an anonymous parameterless function that always returns 2. As we've assigned it to a variable named two, we can say that the function is not anonymous anymore, and we can use the name to invoke it.
# the second one is a one-parameter anonymous function that returns the value of its squared argument. We've named it as such, too.
# the third lambda takes two parameters and returns the value of the first one raised to the power of the second one. The name of the variable which carries the lambda speaks for itself. We don't use pow to avoid confusion with the built-in function of the same name and the same purpose.

# The program produces the following output:

# 4 4
# 1 1
# 0 0
# 1 1
# 4 4
# output

# This example is clear enough to show how lambdas are declared and how they behave, 
# but it says nothing about why they're necessary, and what they're used for, 
# since they can all be replaced with routine Python functions.

# Where is the benefit?


