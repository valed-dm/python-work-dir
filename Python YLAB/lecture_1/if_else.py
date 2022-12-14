# "Кратко"

# Условная инструкция if-elif-else (её ещё иногда называют оператором ветвления) -
# основной инструмент выбора в Python. Проще говоря, она выбирает, какое действие следует выполнить,
# в зависимости от значения переменных в момент проверки условия.

# "Пример"
# Проверим вхождение некоторого числа в числовой диапазон:

my_age: int = 19

if my_age < 18:
    print('Ты ещё не взрослый', "\n")
elif 17 < my_age < 60:
    print('Добро пожаловать в наш клуб :)', "\n")
else:
    print('Боюсь, Вы слишком старый', "\n")

# "Тернарный оператор"

# В Python существует конструкция, которая по своему действию аналогична конструкции if-else,
# но при этом является выражением. Она называется тернарный оператор. Общий паттерн выглядит так:

my_age: int = 19

is_adult: str = 'Взрослый' if my_age >= 18 else 'Не взрослый'
print("тернарный оператор")
print("is_adult: str = 'Взрослый' if my_age >= 18 else 'Не взрослый' -->", is_adult, "\n")  # Взрослый

# "Множество условий"

# Существуют моменты, когда нам надо проверить несколько условий,
# этого можно достичь с помощью операторов and и or:
my_age: int = 19
my_gender: str = 'male'

if my_age >= 18 and my_gender == 'male':
    print('Взрослый', "\n")
elif my_age >= 18 and my_gender == 'female':
    print('Взрослая', "\n")
else:
    print('В каком роде к вам обращаться?', "\n")

# "Oператоры any() & all()"

# В случаях когда условии для проверки очень много, в Python есть возможность упростить запись кода,
# с помощью операторов:
        # all - должны совпасть все условия
        # any - должно совпасть хотя бы одно условие
        # # Обязательно!: В выше названные операторы следует передавать итерабельные объекты, то есть:
        # list, dict, set, tuple, ...

my_age: int = 19
my_gender: str = 'male'

if all((
    my_age >= 18,
    my_gender == 'male'
)):
    print('Взрослый', "\n")
elif all((
    my_age >= 18,
    my_gender == 'female'
)):
    print('Взрослая', "\n")
else:
    print('В каком роде к вам обращаться?', "\n")


# "Как пишется"

# Схематично структура для создания comprehension выглядит так:

# Сначала записывается часть if с условным выражением, далее могут следовать одна или более необязательных частей
# elif, и, наконец, необязательная часть else. Общая форма записи условной инструкции if выглядит следующим образом:

        # if test1:
        #     state1
        # elif test2:
        #     state2
        # else:
        #     state3
