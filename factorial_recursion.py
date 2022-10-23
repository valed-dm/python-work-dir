def factorial_function(n):
    if n == 1:
        return 1  # The base case (termination condition.)
    return n * factorial_function(n - 1)


print(factorial_function(5))
