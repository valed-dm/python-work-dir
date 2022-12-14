# Кратко

# Python comprehensions - это одна из особенностей языка,
# которая позволяет генерировать определенные структуры данных на основе других итерабельных объектов.
# Это может быть очень полезно, когда надо изменить (отфильтровать) уже существующие данные.

# Пример
# Пусть у нас будет список имен студентов.

students: list[str] = ['Anderson', 'John', 'Doe', 'Alex', 'Gordon', 'Lorem']

# Фильтруем список студентов и получаем только те имена, которые состоят из 4 букв.

students_with_four_letter_names: list[str] = [
    name for name in students if len(name) == 4
]

# Результат будет ['John', 'Alex'].

# Без подобного синтаксиса, код выглядел бы следующим образом

students_with_four_latter_names: list[str] = []
for name in students:
    if len(name) == 4:
        students_with_four_latter_names.append(name)

# Гвидо против: map, filter, reduce Секция статьи "Гвидо против: map, filter, reduce"

# Как пишется

# Схематично структура для создания comprehension выглядит так:
# Обычно
    # [<output> for i in <collection>]

# для словарей
    # {<k:v> for k, v in <collection>}

# для множеств
    # {<output> for i in <collection>}

# с условием
    # [<output> for i in <collection> if <condition>]

# несколько коллекции
    # [<output> for i in <collection1> for j in <collection2>]


# Подводный камень с кортежами (tuple).

# Внимание!!! нет tuple comprehension.
# Чтобы получить кортеж, то синтаксисом будет:

work_marks = ['Anderson', 'John', 'Doe', 'Alex', 'Gordon', 'Lorem']

tuple(name.lower() for name in work_marks)

# Если попробовать записать

marks: tuple[str, ...] = (name for name in work_marks)

# То будет создан генератор

print(work_marks)
print(marks)
# <generator object <genexpr> at 0x7f5d4eb4bf50>

# Подобный синтаксис называется - выражение генератора (generator expression).
# Чтобы получить значения из генератора, используйте метод next()

# print("length", len(marks)) --> TypeError: object of type 'generator' has no len()
print(next(marks))
print(next(marks))
print(next(marks))
print(next(marks))
print(next(marks))
print(next(marks))

print(next(marks)) # --> StopIteration
print(next(marks))
