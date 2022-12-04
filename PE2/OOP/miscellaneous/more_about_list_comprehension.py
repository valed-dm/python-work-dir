# You should be able to remember the rules governing the creation and use of a very special Python phenomenon named list comprehension - a simple and very impressive way of creating lists and their contents.

# In case you need it, we've provided a quick reminder in the editor.

# There are two parts inside the code, both creating a list containing a few of the first natural powers of ten.

# The former uses a routine way of utilizing the for loop, while the latter makes use of the list comprehension and builds the list in situ, without needing a loop, or any other extended code.

# It looks like the list is created inside itself - it's not true, of course, as Python has to perform nearly the same operations as in the first snippet, but it is indisputable that the second formalism is simply more elegant, and lets the reader avoid any unnecessary details.

# The example outputs two identical lines containing the following text:

# [1, 10, 100, 1000, 10000, 100000]
# [1, 10, 100, 1000, 10000, 100000]

# Run the code to check if we're right.

list_1 = []

for ex in range(6):
    list_1.append(10 ** ex)

list_2 = [10 ** ex for ex in range(6)]

print(list_1)
print(list_2)

# More about list comprehensions: continued
# There is a very interesting syntax we want to show you now. Its usability is not limited to list comprehensions, but we have to admit that comprehensions are the ideal environment for it.

# It's a conditional expression - a way of selecting one of two different values based on the result of a Boolean expression.

# Look:

#  ----->>> expression_one if condition else expression_two <<<---------

# It may look a bit surprising at first glance, but you have to keep in mind that it is not a conditional instruction. Moreover, it's not an instruction at all. It's an operator.

# The value it provides is equal to expression_one when the condition is True, and expression_two otherwise.

# A good example will tell you more. Look at the code in the editor.

# The code fills a list with 1's and 0s - if the index of a particular element is odd, the element is set to 0, and to 1 otherwise.

# Simple? Maybe not at first glance. Elegant? Indisputably.

# Can you use the same trick within a list comprehension? Yes, you can.

the_list = []

for x in range(20):
    the_list.append(1 if x % 2 == 0 else 0)

print(the_list)

print()

# Look at the example in the editor.
# Compactness and elegance - these two words come to mind when looking at the code.

the_list = [1 if x % 2 == 0 else 0 for x in range(10)]

print(the_list)
print()

# So, what do they have in common, generators and list comprehensions? Is there any connection between them? Yes. A rather loose connection, but an unequivocal one.
# Just one change can turn any list comprehension into a generator.

# List comprehensions vs. generators
# Now look at the code below and see if you can find the detail 
# that turns a list comprehension into a generator:

the_list = [1 if x % 2 == 0 else 0 for x in range(10)]
the_generator = (1 if x % 2 == 0 else 0 for x in range(10))

for v in the_list:
    print(v, end=" ")
print()

for v in the_generator:
    print(v, end=" ")
print()

# It's the parentheses. The brackets make a comprehension, the parentheses make a generator.
# The code, however, when run, produces two identical lines:

# 1 0 1 0 1 0 1 0 1 0
# 1 0 1 0 1 0 1 0 1 0
# output

# How can you know that the second assignment creates a generator, not a list?
# There is some proof we can show you. Apply the len() function to both these entities.

print(len(the_list))
# print(len(the_generator)) # TypeError: object of type 'generator' has no len()

# Of course, saving either the list or the generator is not necessary - you can create them exactly in the place where you need them - just like here:

for v in [1 if x % 2 == 0 else 0 for x in range(10)]:
    print(v, end=" ")
print()

for v in (1 if x % 2 == 0 else 0 for x in range(10)):
    print(v, end=" ")
print()


# Note: the same appearance of the output doesn't mean that both loops work in the same way. In the first loop, the list is created (and iterated through) as a whole - it actually exists when the loop is being executed.
# In the second loop, there is no list at all - there are only subsequent values produced by the generator, one by one.
# Carry out your own experiments.

