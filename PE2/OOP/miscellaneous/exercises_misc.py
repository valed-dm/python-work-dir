# Exercise 1
# What is the expected output of the following code?

class Vowels:
    def __init__(self):
        # Yes, we know that y is not always considered a vowel.
        self.vow = "aeiouy "
        self.pos = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.pos == len(self.vow):
            raise StopIteration
        self.pos += 1
        return self.vow[self.pos - 1]


vowels = Vowels()
for v in vowels:
    print(v, end=' ')

print('\n------------------------------------')

# Exercise 2
# Write a lambda function, setting the least significant bit of its integer argument,
# and apply it to the map() function to produce the string 1 3 3 5 on the console.

any_list = [1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14]
# even_list =  list(map(lambda x: x if x%2 != 0 else x + 1, any_list)) # Complete the line here.
# binary or in Python --> | <--
even_list = list(map(lambda n: n | 1, any_list))
for x in even_list:
    print(str(x), end=' ')

print('\n------------------------------------')

# Exercise 3
# What is the expected output of the following code?


def replace_spaces(replacement='*'):
    def new_replacement(text):
        return text.replace(' ', replacement)
    return new_replacement


stars = replace_spaces()
at_sign = replace_spaces('@')
print(stars("And Now for Something Completely Different"))
print(at_sign("And Now for Something Completely Different"))

print('------------------------------------')

# PEP 8, the Style Guide for Python Code, recommends that lambdas should not be assigned to variables,
# but rather they should be defined as functions.
# This means that it is better to use a def statement,
# and avoid using an assignment statement that binds a lambda expression to an identifer.
# For example:

# Recommended:


def f(x): return 3*x


print(f(5))

# Not recommended:


def f(x): return 3*x


print(f(7))


# Binding lambdas to identifiers generally duplicates the functionality of the def statement.
# Using def statements, on the other hand, generates more lines of code.
# It is important to understand that reality often likes to draw its own scenarios,
# which do not necessarily follow the conventions or formal recommendations.
# Whether you decide to follow them or not will depend on many things:
# your preferences, other conventions adopted, company internal guidelines,
# compatibility with existing code, etc.
#
# Be aware of this.
