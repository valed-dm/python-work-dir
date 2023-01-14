# Задача №3.

# Написать метод zeros, который принимает на вход целое число (integer)
# и возвращает количество конечных нулей в факториале (N! = 1 * 2 * 3 * ... * N) заданного числа:
# Будьте осторожны 1000! имеет 2568 цифр.

# Доп. инфо: http://mathworld.wolfram.com/Factorial.html

# zeros(6) = 1

# 6! = 1 * 2 * 3 * 4 * 5 * 6 = 720 --> 1 trailing zero

# zeros(12) = 2

# 12! = 479001600 --> 2 trailing zeros

# Подсказка: вы не должны вычислять факториал. Найдите другой способ найти количество нулей.
# алгоритм:
# q_zeros = n // 5 + n // 25 + n // 125 ...


# Основа:

def zeros(n):
    if (n < 0):
        return -1

    q_zeros = 0

    while (n >= 5):
        n //= 5
        q_zeros += n

    # for i in range(n):
    #     if n // 5 ** (i+1) >= 1:
    #         q_zeros += n // 5 ** (i+1)
    #     else:
    #         break

    return q_zeros


# Для проверки:


assert zeros(0) == 0
assert zeros(6) == 1
assert zeros(11) == 2
assert zeros(30) == 7

for i in range(100):
    print("factorial of", i, "has", zeros(i), "trailing zeros")

print("factorial of", 1000, "has", zeros(1000), "trailing zeros")
