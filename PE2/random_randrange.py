# The randrange and randint functions

# If you want integer random values, one of the following functions would fit better:

# randrange(end)
# randrange(beg, end)
# randrange(beg, end, step)
# randint(left, right)

# The first three invocations will generate an integer taken (pseudorandomly) from the range (respectively):
# range(end)
# range(beg, end)
# range(beg, end, step)
# Note the implicit right-sided exclusion!!!!!!

# The last function is an equivalent of randrange(left, right+1) - it generates the integer value i, which falls in the range [left, right] (no exclusion on the right side).

from random import randrange, randint

print(randrange(1), end=' ')
print(randrange(0, 1), end=' ')
print(randrange(0, 1, 1), end=' ')
print(randint(0, 1))


print(randrange(100), end=' ')
print(randrange(50, 100), end=' ')
print(randrange(0, 50, 3), end=' ')
print(randint(0, 100))

# seq = range(0, 100)
# print("seq", seq) ???output