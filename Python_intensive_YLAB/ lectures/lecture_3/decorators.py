# Кратко

# Декораторы — это один из паттернов разработки, своего рода "обёртки", 
# которые дают нам возможность изменить поведение функции, не изменяя её код.

# Для того чтобы понять, как работают декораторы, в первую очередь следует помнить, 
# что функции в python являются объектами, соответственно, их можно возвращать из другой функции 
# или передавать в качестве аргумента. 
# Также, функция в python может быть определена и внутри другой функции.

# Пример

# Напишем декоратор, который будет замерять время выполнения программы.

import time

def my_decorator(func):
    # Внутри себя декоратор определяет функцию-"обёртку". Она будет обёрнута вокруг декорируемой функций,
    # получая возможность исполнять произвольный код до и после неё.
    def wrapper(*args, **kwargs):  # аргументы функции
        start_t = time.perf_counter()
        print("Я - код, который отработает до вызова функции")
        result = func(*args, **kwargs) # Сама функция
        print("Результат функций:", result)
        print("А я - код, срабатывающий после функции")
        end_t = time.perf_counter()
        print("Время выполнения функций:", end_t - start_t)
        return result
    # Вернём эту функцию
    return wrapper

@my_decorator  # <- наш декоратор
def say_hello() -> str:
    time.sleep(3)
    return "hello"

say_hello()

# Результат:

# Я - код, который отработает до вызова функции
# Результат функций: hello
# А я - код, срабатывающий после
# Время выполнения функций: 3.009909


# Дополнительно

# Вот так можно было записать предыдущий пример, не используя синтаксис декораторов:

import time

def my_decorator(func):
    def wrapper(*args, **kwargs):
        start_t = time.perf_counter()
        print("Я - код, который отработает до вызова функции")
        result = func(*args, **kwargs)
        print("Результат функций:", result)
        print("А я - код, срабатывающий после функции")
        end_t = time.perf_counter()
        print("Время выполнения функций:", end_t - start_t)
        return result
    return wrapper

def say_hello() -> str:
    time.sleep(3)
    return "hello"

say_hello = my_decorator(say_hello)
say_hello()