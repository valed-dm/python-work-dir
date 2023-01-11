# https://www.freecodecamp.org/news/python-decorators-explained-with-examples/

# --------------------------------------------------------------------
from time import perf_counter
import tracemalloc
from functools import wraps
from datetime import datetime


def my_decorator_func(func):

    def wrapper_func():
        # Do something before the function.
        func()
        # Do something after the function.
    return wrapper_func


@my_decorator_func
def my_func():
    pass


# --------------------------------------------------------------------
def my_decorator_func(func):

    def wrapper_func(*args, **kwargs):
        # Do something before the function.
        func(*args, **kwargs)
        # Do something after the function.
    return wrapper_func


@my_decorator_func
def my_func(my_arg):
    '''Example docstring for function'''
    pass


# --------------------------------------------------------------------
def friendly_reminder(func):
    '''Reminder for husband'''
    func()
    print('Don\'t forget to bring your wallet!')


def action():
    print('I am going to the store buy you something nice.')


friendly_reminder(action)

# --------------------------------------------------------------------


def log_datetime(func):
    '''Log the date and time of a function'''

    def wrapper():
        print(f'{"-"*30}')
        print(
            f'Function: {func.__name__}\nRun on: {datetime.today().strftime("%Y-%m-%d %H:%M:%S")}')
        func()
        print(f'{"-"*30}')
    return wrapper


@log_datetime
def daily_backup():

    print('Daily backup job has finished.')


daily_backup()
# --------------------------------------------------------------------

# Here is a decorator with arguments:


# def my_decorator_func(func):

#     def wrapper_func(*args, **kwargs):
#         # Do something before the function.
#         func(*args, **kwargs)
#         # Do something after the function.
#     return wrapper_func


# @my_decorator_func
# def my_func(my_arg):
#     '''Example docstring for function'''

#     pass


# Decorators hide the function they are decorating. 
# If I check the __name__ or __doc__ method we get an unexpected result.

# print(my_func.__name__)
# print(my_func.__doc__)

# # Output

# wrapper_func
# None


# To fix this issue I will use functools. 
# Functools wraps will update the decorator with the decorated functions attributes.


# from functools import wraps

# def my_decorator_func(func):

#     @wraps(func)
#     def wrapper_func(*args, **kwargs):
#         func(*args, **kwargs)
#     return wrapper_func

# @my_decorator_func
# def my_func(my_args):
#     '''Example docstring for function'''

#     pass


# Now I receive the output I am expecting.

# print(my_func.__name__)
# print(my_func.__doc__)

# # Output

# my_func
# Example docstring for function

# --------------------------------------------------------------------

def measure_performance(func):
    '''Measure performance of a function'''

    @wraps(func)
    def wrapper(*args, **kwargs):
        tracemalloc.start()
        start_time = perf_counter()
        func(*args, **kwargs)
        current, peak = tracemalloc.get_traced_memory()
        finish_time = perf_counter()
        print(f'Function: {func.__name__}')
        print(f'Method: {func.__doc__}')
        print(f'Memory usage:\t\t {current / 10**6:.6f} MB \n'
              f'Peak memory usage:\t {peak / 10**6:.6f} MB ')
        print(f'Time elapsed is seconds: {finish_time - start_time:.6f}')
        print(f'{"-"*40}')
        tracemalloc.stop()
        return "string from wrapper return clause"
    return wrapper


@measure_performance
def make_list1():
    '''Range'''

    my_list = list(range(100000))


@measure_performance
def make_list2():
    '''List comprehension'''

    my_list = [l for l in range(100000)]


@measure_performance
def make_list3():
    '''Append'''

    my_list = []
    for item in range(100000):
        my_list.append(item)


@measure_performance
def make_list4():
    '''Concatenation'''

    my_list = []
    for item in range(100000):
        my_list = my_list + [item]


print(make_list1())
print(make_list2())
print(make_list3())
print(make_list4())
