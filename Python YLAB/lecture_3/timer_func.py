# Timer Function using Decorator

# The timer function is one of the applications of decorators.
# In the below example, we have made a timer_func function that accepts a function object func.
# Inside the timer function, we have defined wrap_func which can take any number of arguments (*args)
# and any number of keyword arguments (**kwargs) passed to it. We did this to make our timer_func more flexible.

# In the body of wrap_func, we recorded the current time t1 using the time method of the time module,
# then we have called the function func passing the same parameters (*args, **kwargs)
# that were received by wrap_func and stored the returned value in the result.
# Now we have again recorded the current time t2 and printed the difference between the recorded times
# i.e. { t2 – t1 } with precision up to the 4th decimal place.
# This {t2 – t1} is the time passed during the execution of the function func.
# At last, we have returned the result value inside wrap_func function and returned this wrap_func function
# inside timer_func function.

# We have also defined the long_time function using @timer_func decorator,
# so whenever we call long_time function it will be called like :

# timer_func(long_time)(5)
# The timer_func function when called passing long_time as a parameter returns a wrap_func function
# and a function object func starts pointing to the long_time function.

# wrap_func(5)
# Now the wrap_func will execute as explained above and the result is returned.

from time import time


def timer_func(func):
    # This function shows the execution time of
    # the function object passed
    def wrap_func(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        print(f'Function {func.__name__!r} executed in {(t2-t1):.4f}s')
        return result
    return wrap_func


@timer_func
def long_time(n):
    for i in range(n):
        for j in range(100000):
            i*j


long_time(5)
