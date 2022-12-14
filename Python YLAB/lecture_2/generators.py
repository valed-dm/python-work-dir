# Кратко

# Генератор — это функция, которая умеет возвращать несколько значений по очереди,
# не храня в памяти весь набор значений.

# Пример

# Вернёмся к вашей реализации Range: у вас есть класс, который умеет возвращать следующее число в заданном диапазоне.
# В методе __next__ вы каждый раз высчитываете актуальное значение и возвращаете его пользователю.
# Формально это можно назвать генератором.

# Но в Python для создания генераторов используется особый, упрощенный синтаксис.

# Давайте посмотрим, как тот же самый код будет выглядеть, если написать его с использованием генератора.

def gen_range(stop_value):
    stop_value = stop_value - 1
    current = -1
    while current < stop_value:
        current += 1
        yield current

# Запустим код и убедимся в этом.


for x in gen_range(5):
    print("gen_range {}:".format(x), x)
# 0
# 1
# 2

for x in range(5):
    print("range {}:".format(x), x)# Как это работает

# Работа генераторов построена на принципе запоминания контекста выполнения функции.
# Если не вдаваться в подробности работы Python-интерпретатора, то функция-генератор «запоминает»,
# в каком месте она остановилась, и может продолжить своё выполнение после ключевого слова yield.


def simple_generator():
    yield 1
    yield 2
    yield 3
    yield 4
    return 5

# Рассмотрим, как поведёт себя генератор с несколькими yield:
# Изучая итераторы вы узнали, что доставать из него значения можно вручную с помощью метода next
# или циклом, а ещё неявно — в цикле.

# Генератор предоставляет те же возможности: любой генератор является итератором.
# В предыдущем примере вы воспользовались циклом, 
# а сейчас, для разнообразия, достанем элементы вручную:

gen = simple_generator()

print("next:", next(gen))
print("next:", next(gen))
print("next:", next(gen))
print("next:", next(gen))
print("next:", next(gen))

# В результате вы увидите следующее:

# 1
# 2
# Traceback (most recent call last):
# ...
# StopIteration: 3

# То есть функция действительно запоминает, где она остановилась после каждого вызова функции next.
# Генераторы удобны и для создания генераторных выражений — generator expressions.
# Особенно это полезно, если нужно сгенерировать много объектов, а память расходовать жалко. 
# Код выглядит так:

gen_exp = (x for x in range(100000))
print(gen_exp)
# <generator object <genexpr> at 0x10c4496d0>

# Полезные ссылки

# Как использовать генераторы и yield на Python: https://realpython.com/introduction-to-python-generators/
# Основной PEP на тему генераторов: https://peps.python.org/pep-0255/
