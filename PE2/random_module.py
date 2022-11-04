# import random

# for name in dir(random):
#     print(name)

# from random import random
# for i in range(5):
#     print(random())


# Due to the fact that the seed is always set with the same value, the sequence of generated values always looks the same.
from random import random, seed
seed(0)
for i in range(5):
    print(random())

# 0.8444218515250481
# 0.7579544029403025
# 0.420571580830845
# 0.25891675029296335
# 0.5112747213686085