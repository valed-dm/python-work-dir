import pandas as pd


class A(object):
    def __init__(self):
        print("A -> ", end=" ")


class B(A):
    def __init__(self):
        print("B -> ", end=" ")
        super(B, self).__init__()


class C(A):
    def __init__(self):
        print("C -> ", end=" ")
        super(C, self).__init__()


class D(B, C):
    def __init__(self):
        print("D -> ", end=" ")
        super(D, self).__init__()


d = D()


def f(a, b):
    if b == 1:
        return a
    if b % 2 == 0:
        return f(a*a, b/2)
    else:
        return a*f(a, b-1)


print(f(2, 3))

# df = pd.DataFrame({'grps': list('aaabbcaabcccbbc'),
#                    'vals': [12, 345, 3, 1, 45, 14, 4, 52, 54, 23, 235, 21, 57, 3, 87]})

# df.groupby('grp')['vals'].nlargest(3).sum(level=0)

def variadac(*a):
    print(a)
 
variadac(*"abc")
