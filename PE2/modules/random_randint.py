# The previous functions have one important disadvantage - they may produce repeating values even if the number of subsequent invocations is not greater than the width of the specified range.
# Look at the code below - the program very likely outputs a set of numbers in which some elements are not unique:

from random import randint

for i in range(10):
    print(randint(8, 10), end=', ')
print('\n----------------')

from random import choice, sample

# The first variant chooses a "random" element from the input sequence and returns it.
# The second one builds a list (a sample) consisting of the elements_to_choose element "drawn" from the input sequence.
# In other words, the function chooses some of the input elements, returning a list with the choice. The elements in the sample are placed in random order. Note: the elements_to_choose must not be greater than the length of the input sequence.

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(choice(my_list))
print(sample(my_list, 5))
print(sample(my_list, 10))