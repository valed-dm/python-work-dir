# 1. Задача на декоратор с кешированием результата.

# Напишите функцию-декоратор, которая сохранит (закэширует)
# значение декорируемой функции multiplier (Чистая функция).
# Если декорируемая функция будет вызвана повторно с теми же параметрами
# — декоратор должен вернуть сохранённый результат, не выполняя функцию.

# В качестве структуры для кэша, можете использовать словарь в Python.

# *В качестве задания со звездочкой можете использовать вместо Python-словаря => Redis.


# Основа:
import redis
from functools import wraps


def cache(func):
    cache = dict()

    @wraps(func)
    def wrapper(*args, **kwargs):
        # Do something before the function.
        key = str(args[0])

        if key in cache:
            print(f"cached value returned: {cache[key]}")
            return cache[key]
        else:
            res = func(*args, **kwargs)
            print(f"multiplier({key}) = {res}")

        # Do something after the function.
        cache[key] = res
        print(f"cache content: {cache}")

        return res

    return wrapper


def cache_redis(func):
    r = redis.Redis(db=0)

    @wraps(func)
    def wrapper(*args, **kwargs):
        # Do something before the function.
        redis_dict = dict()
        key: str = str(args[0])
        val: bytes = r.get(key)

        def r_data_print():
            for k in r.keys():
                crit = r.type(k).decode('utf-8') 
                if crit == "string":
                    k = k.decode('utf-8')
                    if k.isdigit():
                        redis_dict[k] = r.get(k).decode('utf-8')

            print(f"cache content: {redis_dict}")

        if val:
            r_data_print()
            val: int = val.decode('utf-8')
            print(f"cached value returned: {val}")
            return val
        else:
            res: int = func(*args, **kwargs)
            print(f"multiplier({key}) = {res}")

        # Do something after the function.
        r.mset({key: res})
        r_data_print()

        return res

    return wrapper


@cache_redis
def multiplier(number: int):
    '''multiplier pure function'''

    return number * 2


multiplier(50)
multiplier(100)
multiplier(200)
multiplier(300)
multiplier(400)
multiplier(100)
multiplier(200)
multiplier(300)
multiplier(400)
multiplier(500)
print(f"multiplier(100) returned value = {multiplier(100)}")
print(multiplier.__name__)
print(multiplier.__doc__)
