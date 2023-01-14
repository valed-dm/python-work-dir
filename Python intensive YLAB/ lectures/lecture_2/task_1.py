# 1. Задача на циклический итератор.

# Надо написать класс CyclicIterator.

# Итератор должен итерироваться по итерируемому объекту (list, tuple, set, range, Range2, и т. д.),
# и когда достигнет последнего элемента, начинать сначала.

# cyclic_iterator = CyclicIterator(range(3))
# for i in cyclic_iterator:
#     print(i)

# Основа:
from itertools import cycle

class CyclicIterator:
    def __init__(self, iterable):
        self.iterator = cycle(iterable)

    def __iter__(self):
        return self

    def __next__(self):
       return next(self.iterator)


cyclic_iterator = CyclicIterator(range(3))
for i in cyclic_iterator:
    print(i)

# Для проверки. Ожидаемый вывод программы:

# 0
# 1
# 2
# 0
# 1
# 2
# 0
# 1
# 2
# ....
