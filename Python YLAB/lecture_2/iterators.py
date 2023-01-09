# Кратко

# Разработчики используют итераторы в коде настолько часто, что даже не задумываются,
# в чём они помогают. Итераторы в Python — это списки, словари, множества, строки,
# файлы и другие коллекции. Везде, где вы пишете цикл for, используется итератор.
# Итераторы помогают перемещаться по объектам любого контейнера в коде.
# При этом вам не нужно задумываться о том, как хранятся и обрабатываются эти элементы:
# итератор инкапсулирует их. Проще говоря, это способ вычитывать элементы из объекта по одному.

# Пример

# Представим, что на собеседовании вас попросили реализовать аналог функции range.
# Попробуем быстро его написать.

class Range:
    def __init__(self, stop_value: int):
        self.current = -1
        self.stop_value = stop_value - 1

    def __iter__(self):
        return RangeIterator(self)


class RangeIterator:
    def __init__(self, container):
        self.container = container

    def __next__(self):
        print("RI SC = ", "CURR = ",self.container.current, "STOP = ", self.container.stop_value)
        if self.container.current < self.container.stop_value:
            self.container.current += 1
            return self.container.current
        raise StopIteration

# Запустим код и убедимся в этом.


_range = Range(10)
for i in _range:
    print("Range1", i, end=' ')

print("\n--------------------------------------")
# В итоге вы получаете числа от 0 до 9 на отдельных строках.



# Как это работает

# Начнём с класса Range.
# У него внутри реализован магический метод __iter__.
# Он обозначает, что объект этого класса итерабельный, то есть с ним можно работать в цикле for.
# Ещё говорят, что __iter__ отдаёт итерирующий объект(итератор).

# Ограничимся понятиями итератора и итерабельного объекта.

# Чтобы код действительно отдавал новые данные из _range,
# нужно реализовать соответствующую функцию. Она как раз и называется итератор.
# RangeIterator — итератор для класса Range.
# Любой итератор должен реализовывать магическую функцию __next__,
# в которой он должен отдавать новые значения для объектов класса Range.
# Если вы дошли до конца множества значений, то появляется исключение StopIteration.

# Для тех, кто привык читать первоисточники, существует PEP-234 (на английском).
# Там подробно изложена работа итераторов и итерабельных объектов.

# Можно упростить

# В Python есть возможность объявить объекты класса и итерабельными, и итераторами.
# Это удобно, но с точки зрения принципов проектирования приложения,у такого объекта есть две ответственности: 
# он является итератором и при этом выполняет какую-то свою логику. В мире Python это допустимо,
# но в некоторых других языках вас могут понять неправильно. 
# Будьте бдительны!


class Range2:
    def __init__(self, stop_value: int):
        self.current = -1
        self.stop_value = stop_value - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.stop_value:
            self.current += 1
            return self.current
        raise StopIteration

# Цикл for под капотом.

# Также использует методы итератора


iterable = Range2(10)
iterator = iter(iterable)
# print("Range2:", list(iterator))

while True:
    count = 0
    try:
        # count += 1
        print("while attempt count:", count)  
        value = next(iterator)
        count += 1
        print("while", value, end=", ") # StopIteration error has been raised above in Range2
        
    except StopIteration:
        break

# Полезные ссылки

# Пошаговое знакомство с итераторами в Python --> https://dbader.org/blog/python-iterators
# Подробная статья об итераторах с примерами --> https://techbeamers.com/python-iterator/
