# 2. Задача на декоратор с параметрами.

# Надо написать декоратор для повторного выполнения декорируемой функции через некоторое время.
# Использует наивный экспоненциальный рост времени повтора (factor)
# до граничного времени ожидания (border_sleep_time).

# В качестве параметров декоратор будет получать:

# call_count - число, описывающее кол-во раз запуска функций;
# start_sleep_time - начальное время повтора;
# factor - во сколько раз нужно увеличить время ожидания;
# border_sleep_time - граничное время ожидания.

# Формула:

# t = start_sleep_time * 2^(n) if t < border_sleep_time
# t = border_sleep_time if t >= border_sleep_time

# Ожидаемый результат:

# Кол-во запусков = call_count (допустим 3)
# Начало работы
# Запуск номер 1. Ожидание: t секунд. Результат декорируемой функций = func_result.
# Запуск номер 2. Ожидание: t секунд. Результат декорируемой функций = func_result.
# ...
# Конец работы

from time import time, sleep


def decorator(*args, **kwargs):
    '''This decorator provides periodic execution of passed function'''

    def timer_func(func):
        '''This function shows the execution time of the function object passed'''

        def wrap_func(*args, **kwargs):
            t1 = time()
            result = func(*args, **kwargs)
            t2 = time()
            print(f'Function {func.__name__!r} executed in {(t2-t1):.4f}s')
            return result

        return wrap_func

    @timer_func
    def delay_func(func, n, delay):
        '''Delays passed function ecxecution'''

        sleep(delay)
        print(f"in a {n} time after delay {delay} we obtain -->", end=" ")
        func()

    @timer_func
    def inner(func):
        '''Contains delay logic and invokes delay_func'''

        for i in range(kwargs["call_count"]):
            t = kwargs["start_sleep_time"]*kwargs["factor"]**(i+1)
            delay = t if t < kwargs["border_sleep_time"] else kwargs["border_sleep_time"]
            delay_func(func, (i + 1), delay)

    return inner


@decorator(call_count=6, start_sleep_time=.1, factor=2, border_sleep_time=2.5)
def my_func():
    print("my_func result")
