def fib(n):
    if n == 0:
        return None
    if n < 3:
        return 1
    return fib(n - 1) + fib(n - 2)

for n in range(11):
    print(n, "-> ", fib(n))
