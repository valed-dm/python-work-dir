# Q1: What is expected output of the following code?

def my_fun():
    for num in range(3):
        yield num


for i in my_fun():
    print(i, end=' ')

print('\n----------------')

# Q2: What is expected output of the following code?

foo = [i + i for i in range(5)]
print(foo)

print('----------------')

# Q3: What is expected output of the following code?


def x(a, b): return a ** b


print(x(2, 10))

print('----------------')

# Q4:
# the map() function can accept only two args
# the first map() function arg can be a list
# the map() function can accept more than two args --> !>yes<!
# the second map() function arg can be a list --> !>yes<!

print(list(map(lambda x, y: x*y, [1, 2, 3], (10,20,30,40))))

print('----------------')

# Q5:
# the filter() function returns an iterator --> !>yes<! 
# the filter() function syntax --> filter(function, iterable) --> !>yes<! 
# the filter() function does not return an iterator
# the filter() function syntax --> filter(iterable, function)


# Q6: What is expected output of the following code?

numbers = (1,2,5,9,15)

def filter_numbers(num):
    nums = (1,5,17)
    if num in nums:
        return True
    else:
        return False

f_numbers = filter(filter_numbers, numbers) # returns an iterator stored in f_numbers var

for n in f_numbers:
    print(n)

print('----------------')

# Q7: Which of the following statements are true?

# The declaration of a lambda function is the same as the declaration of a regular function
# The yield statement must be used outside functions
# The map() function creates a copy of its second arg, and applies first argument to it --> !>yes<!
# A list comprehension becomes a generator when used inside round brackets --> !>yes<!

# Q8: The two basic, mutually exclusive, file open modes are named as
# binary and text

# Q9: What happened if you run following code, assuming that the directory в already exist?

import os

os.mkdir('./test_dir')
os.makedirs("./a/b/c/d") # FileExistsError: [Errno 17] File exists: './a/b/c/d'

