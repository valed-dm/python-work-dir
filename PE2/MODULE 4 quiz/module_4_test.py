# import os

# os.mkdir('pictures')
# os.chdir('pictures')
# os.mkdir('thumbnails')
# os.chdir('thumbnails')
# os.mkdir('tmp')
# os.chdir('../')

# print(os.getcwd()) # /Users/dmitrijvaledinskij/Python/pictures

print('----------------')

my_tuple = (0,1,2,3,4,5,6)

foo = tuple(filter(lambda x: x>1, my_tuple))
print(foo)
foo = list(filter(lambda x: x>1, my_tuple))
print(foo)

print('----------------')

b = bytearray(3)
print(b)

for b in b:
    print(b)
    print(hex(b))

print('----------------')

from datetime import date

date_1 = date(1992, 1 , 16)
date_2 = date(1991, 2, 5)

print(date_1 - date_2)

print('----------------')

def I():
    s = 'abcdef'
    for с in s[::2]:
        yield с

for x in I():
    print(x, end='')

print('\n----------------')

def fun(n):
    s = '+'
    for i in range(n):
        s += s
        yield s

for x in fun(2):
    print(x, end='')

print('\n----------------')