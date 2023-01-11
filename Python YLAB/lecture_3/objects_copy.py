# Кратко

# Когда речь заходит о копирований объектов, в Python используют 2 способа копирования:
# Поверхностное копирование (shallow copy)
# Глубокое копирование (deep copy)


# Поверхностное копирование:


# Создает отдельный новый объект или список, но вместо копирования дочерних элементов в новый объект,
# оно просто копирует ссылки на их адреса памяти.
# Следовательно, если вы сделаете изменение в исходном объекте,
# оно будет отражено в скопированном объекте, и наоборот.

# Пример

# Представим студента факультета инженерии и естественных наук по имени Алекс.
# У него есть определенный список предметов на курс, которые он должен посещать.
# Спустя время, у Алекса появился новый согруппник Петя.
# Так как они оба на одной специальности, Пете тоже нужны эти предметы.
# Плюс, их обоих записали на курсы английского.

import copy

# Предметы Алекса
alex_lessons: dict[str, list[str]] = {
    "semester1": ["Экономика", "Математика 1", "Физика 1"],
    "semester2": ["Сопромат", "Математика 2", "Физика 2"],
}

alex_lessons.get("semester1", []).append("Английский")

# Предметы Пети
petya_lessons: dict[str, list[str]] = copy.copy(
    alex_lessons)  # Предметы Олега (скопированы из списка Алекса)

print("Alex's lessons: ", alex_lessons)
print("---------------------------------")
print("Petya's lessons: ", petya_lessons)
print("---------------------------------")


# Глубокое копирование


# Создает новую и отдельную копию всего объекта или списка со своим уникальным адресом памяти.
# Это означает, что любые изменения, внесенные вами в новую копию объекта или списка,
# не будут отражаться в исходной. Этот процесс происходит следующим образом:
# сначала создается новый список или объект, а затем рекурсивно копируются все элементы
# из исходного объекта в новый.

# Пример

# Давайте представим что у нас есть списки оценок Алисы, а также список Олега,
# который списывал всё у Алисы. Спустя какое-то время Олег самостоятельно получил ещё одну оценку
# в свой список.
# Как это будет выглядеть:

alisa_grades: list[int] = [90, 85, 82]  # Оценки Алисы
# Оценки Олега (скопированы из списка Алисы)
oleg_grades: list[int] = copy.deepcopy(alisa_grades)

oleg_grades.insert(2, 95)

print("Alisa's grades: ", alisa_grades)
print("---------------------------------")
print("Oleg's grades: ", oleg_grades)


# Дополнительно


# Бывают случаи когда надо создать поверхностную копию списка. Сделать это можно с помощью:

# Сделать slice списка;
first_list: list[int] = [1, 2, 3, 4]
second_list = first_list[:]
# second_list = first_list
second_list.insert(1, 123)
print("---------------------------------")
print(first_list, second_list)

# Метод copy() у списка;
first_list: list[int] = [1, 2, 3, 4]
second_list = first_list.copy()


# Использовать built-in метод list().
first_list: list[int] = [1, 2, 3, 4]
second_list = list(first_list)


# Initialize list
List = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Show original list
print("\nOriginal List:\n", List)

print("\nSliced Lists: ")

# Display sliced list
print(List[3:9:2])

# Display sliced list
print(List[::2])

# Display sliced list
print(List[::])


# Initialize list
List = ['Geeks', 4, 'geeks !']

# Show original list
print("\nOriginal List:\n", List)

print("\nSliced Lists: ")

# Display sliced list
print(List[::-1])

# Display sliced list
print(List[::-3])

# Display sliced list
print(List[:1:-2])


# Initialize list
List = [-999, 'G4G', 1706256, '^_^', 3.1496]

# Show original list
print("\nOriginal List:\n", List)

print("\nSliced Lists: ")

# Display sliced list
print(List[10::2])

# Display sliced list
print(List[1:1:1])

# Display sliced list
print(List[-1:-1:-1])

# Display sliced list
print(List[:0:])
