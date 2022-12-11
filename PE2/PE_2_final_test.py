import random
from datetime import datetime
x = '\\\\'
print(len(x))

print('----------------')


class A:
    A = 1

    def __init__(self):
        self.a = 0


print(hasattr(A, 'a'))  # False

print('----------------')


datetime_1 = datetime(2019, 11, 27, 11, 27, 22)
datetime_2 = datetime(2019, 11, 27, 0, 0, 0)

print(datetime_1 - datetime_2)

print('----------------')

numbers = [i*i for i in range(5)]
print(numbers)

foo = list(map(lambda x: x // 2, numbers))
foo_1 = list(filter(lambda x: x % 2, numbers))  # 0 -> False, 1 -> True !
foo_2 = list(filter(lambda x: x/2, numbers))
foo_3 = list(map(lambda x: x % 2, numbers))


print(foo)  # we need to get [1, 9]
print(foo_1)
print(foo_2)
print(foo_3)

print('----------------')

print(__name__)

print('----------------')


class A:
    pass


class B(A):
    pass


class C(B):
    pass


print(issubclass(A, C))

print('----------------')

# i didn't find right answer in test!
a = random.randrange(10, 100, 3) # start point 10 breaks the needed result
b = random.randint(0, 100)
c = random.choice((0, 100, 3))

print(a, b, c)  # expectations: possible output --> 6 82 0 <--

for i in range(10, 100):
    if i % 3 == 0:
        print(i, end=' ')

print('\n---------------')

class A:
    def __init__(self, v=2):
        self.v = v

    def set(self, v=1):
        self.v += v
        return self.v

a = A()
b = a
b.set()
print(a.v)

print('----------------')

import os
print(os.uname())

print('----------------')

