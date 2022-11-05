from sys import path
# path.append('/Users/dmitrijvaledinskij/Python/PE2/modules')
path.insert(0, './PE2/modules')
import module

zeroes = [0 for i in range(5)]
ones = [1 for i in range(5)]

print(module.suml(zeroes))
print(module.prodl(ones))
print(zeroes, ones)

for p in path:
    print(p)
