import random


# to evaluate sequence i + 3:
def seq(left, right):
    next = 0
    for i in range(left, right):
        if i == left:
            print(i, end=' ')
            next = i + 3
        elif i == next:
            print(next, end=' ')
            next += 3

seq(10, 100)