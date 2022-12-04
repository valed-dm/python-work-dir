# Q1: -------------------------------
class A:
    def __str__(self):
        return 'a'


class B:
    def __str__(self):
        return 'b'


class C(A, B):
    pass


o = C()
print('Q1 --->', o)


# Q2: -------------------------------
class A:
    X = 0

    def __init__(self, v=0):
        self.Y = v
        A.X += v


a = A()
b = A(1)
с = A(2)

print('Q2 --->', с.X)


# Q3: -------------------------------
class A:
    def __init__(self):
        self.a = 1


class B(A):
    def __init__(self):
        # A.__init__(self) # right invocation is to be placed here!
        super().__init__()
        self.b = 2 + self.a * 5


o = B()
print('Q3 --->', str(hasattr(o, 'a')) + ',', 'a =', o.a)
print('Q3 --->', str(hasattr(o, 'b')) + ',', 'b =', o.b)


# Q4: -------------------------------
class I:
    def __init__(self):
        self.s = 'abcdefgh'
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i == len(self.s):
            raise StopIteration
        v = self.s[self.i]
        self.i += 1
        return v


print('Q4 --->  ', end='')

for x in I():
    # what will be the result of executing the following code? ---> abcdefgh
    print(x, end='')

print('  <--- Q4')


# Q5: -------------------------------
class Ex(Exception):
    def __init__(self, msg):
        Exception.__init__(self, msg + msg)  # ---> exex
        self.args = (msg,)  # ---> ex


try:
    raise Ex('ex')
except Ex as e:
    print('Q5 --->', e)
except Exception as e:
    print('Q5 --->', e)


# Q6: -------------------------------
try:
    raise Exception(1, 2, 3)
except Exception as e:
    print('Q6 --->', len(e.args))


# Q7: -------------------------------
print('Q7 --->', 'LIFO is actually a ---> stack <---')


# Q8: -------------------------------
class A:
    v = 2


class B(A):
    v = 1


class C(B):
    pass


o = C()
print('Q8 --->', o.v)


# Q9: -------------------------------
class A:
    def a(self):
        print('Q9 --->', 'a')


class B:
    def a(self):
        print('Q9 --->', 'b')  # this method is being called finally


class C(B, A):
    def c(self):
        self.a()


o = C()
o.c()


# Q10: -------------------------------
class A:
    A = 1


print('Q10 --->', end=' ')
print(hasattr(A, 'A'))


class A:
    def __init__(self):
        pass


# a = A(1) # TypeError: A.__init__() takes 1 positional argument but 2 were given
print('Q11 --->', end=' ')
print('TypeError occured --->', hasattr(a, 'A'))


# Q12: -------------------------------
class A:
    pass


class B(A):
    pass


class C(B):
    pass


print('Q12 --->', issubclass(C, A))


# Q13: -------------------------------
class A:
    def __init__(self, v):
        self.__a = v + 1


a = A(0)
print('Q13 --->', 'AttributeError: \'A\' object has no attribute \'__a\'')
# print('Q13 --->', a.__a)  # AttributeError: 'A' object has no attribute '__a'


# Q14: -------------------------------
def f(x):
    try:
        x = x / x
    except:
        print('a', end='')
    else:
        print('b', end='')
    finally:
        print('c', end='')


print('Q14 ---> ', end='')
f(1)
f(0)  # code outputs bcac


# Q15: -------------------------------
class A:
    def __init__(self, v=1):
        self.v = v

    def set(self, v):
        self.v = v
        return v


a = A()
print('\nQ15 --->', a.set(a.v + 1))


# Q16: -------------------------------
class Class:
    def __init__(self):
        pass


print('Q16 --->', 'object = Class()')


# Q17: -------------------------------
class A:
    def __str__(self):
        return 'a'


class B(A):
    def __str__(self):
        return 'b'


class C(B):
    pass


o = C()
print('Q17 --->', o)
