# Способы форматирования

# В Python существует 5 способов форматирования строк:

# Конкатенация;
# Оператор %;
# Модуль Template;
# Метод format();
# f-строки.




# Конкатенация.

# Конкатенация строк - операция, "склеивающая" несколько строк в одну.
# Грубый способ, который не советуют использовать на практике, т.к. на каждой итераций,
# интерпретатор Python создает новый строковый объект получая сложность алгоритма O(n^2).
# Однако на 2022 год, в последних версиях интерпретатора CPython (интерпретатор по умолчанию),
# этот момент оптимизирован в отличие от других интерпретаторов PyPy, Jython, IronPython, Cython, Psyco и т.д.

import timeit
from string import Template

print("Hello " + "John Doe" + "!")


# В случаях, когда надо превратить в строку массив значений, используйте метод join(),
# где сложность составит O(n)
print("".join(["Hello ", "John Doe", "!"]))




# Оператор %.

# Форматирование с помощью оператора %. Перешел из языка С
print("Hello %s!" % "John Doe")




# Модуль Template.

# Форматирование с помощью модуля Template из основной библиотеки.
# Добавлен в версий 2.4 (PEP292) и являлся заменой оператору %.
my_string = Template("Hello $full_name!")
print(my_string.substitute(full_name="John Doe"))




# Метод format().

# Форматирование с помощью метода format(). Был добавлен уже в Python3
# именованные метки:
print("Hello {name}!".format(name="John Doe"))
# позиционные метки:
print("Hello {0}!".format("John Doe"))
# без меток:
print("Hello {}!".format("John Doe"))




# f-строки.
# f-строки (formatted string). Появился с версий 3.6
name: str = "John Doe"
print(f"Hello {name}!")




# Вывод.


# Проверим скорость форматирования различными способами:


def func1():
    str1, str2, str3 = "text1", "text2", "text3"
    result: str = "str1=%s, str2=%s, str3=%s" % (str1, str2, str3)


def func2():
    str1, str2, str3 = "text1", "text2", "text3"
    result: str = "str1={}, str2={}, str3={}".format(str1, str2, str3)


def func3():
    str1, str2, str3 = "text1", "text2", "text3"
    result: str = f"str1={str1}, str2={str2}, str3={str3}"


times = []
num_runs: int = 100
duration = timeit.Timer(func1).timeit(number=num_runs)
avg_duration = duration / num_runs
times.append(avg_duration * 1000)

duration = timeit.Timer(func2).timeit(number=num_runs)
avg_duration = duration / num_runs
times.append(avg_duration * 1000)

duration = timeit.Timer(func3).timeit(number=num_runs)
avg_duration = duration / num_runs
times.append(avg_duration * 1000)

print(f"operator % => {times[0]} ms")
print(f"method format() => {times[1]} ms")
print(f"f-string => {times[2]} ms")


# Результат:

# operator % => 0.00025000000000000716 ms
# method format() => 0.0002920000000000006 ms
# f-string => 0.00017799999999998373 ms

# В результате самым быстром способом форматирования строк, является f-строка.

# Допустим ты хочешь соединить 3 слова "first" + " second" + " third" - это 3 разных объекта

# Первый "+", "first" + " second", будет создан новый объект "first second"
# Второй "+", "first second" + " third", снова будет создан новый объект "first second third"
# То есть получается от кол-ва слов, которые надо склеить,
# будет также увеличиваться кол-во объектов создаваемых в памяти программы

# В случае с f-строками, интерпретатор пробежится по кол-во слов,
# которые следует склеить и создаст один новый объект. То есть сложность будет O(n),
# неважно сколько слов, на выходе будет один объект.
