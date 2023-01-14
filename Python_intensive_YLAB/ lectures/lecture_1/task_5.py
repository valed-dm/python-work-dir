# Задача №5.

# Написать метод count_find_num, который принимает на вход список простых множителей (primesL)
# и целое число, предел (limit), после чего попробуйте сгенерировать по порядку все числа,
# меньше значения предела, которые имеют все и только простые множители простых чисел primesL.

# primesL = [2, 5, 7]
# limit = 500

# List of Numbers Under 500          Prime Factorization
# ___________________________________________________________
#            70                         [2, 5, 7]
#           140                         [2, 2, 5, 7]
#           280                         [2, 2, 2, 5, 7]
#           350                         [2, 5, 5, 7]
#           490                         [2, 5, 7, 7]

# 5 из этих чисел меньше 500, а самое большое из них 490.

# primesL = [2, 5, 7]
# limit = 500
# count_find_num(primesL, val) == [5, 490]

# Основа:
def calculate_prime_factors(num):
    prime_factors = set()
    prime_factorization = []

    if num % 2 == 0:
        prime_factors.add(2)

    while num % 2 == 0:
        prime_factorization.append(2)
        num = num // 2
        if num == 1:
            return [prime_factors, prime_factorization]

    for factor in range(3, num + 1, 2):
        if num % factor == 0:
            prime_factors.add(factor)
            while num % factor == 0:
                prime_factorization.append(factor)
                num = num // factor
                if num == 1:
                    return [prime_factors, prime_factorization]

# input_number = 198
# output = calculate_prime_factors(input_number)
# print("Prime factors of {} are {}".format(input_number, output))


def print_numbers_list(l: list, limit: int):
    s = 13*" "
    print("Numbers under " + str(limit) + ":" + " "*5 + "Prime Factorization")
    for j in range(len(l)):
        s = s[:13 - len(str(l[j][0]))] + str(l[j][0]) + 11*" " + str(l[j][1])
        print(s)
        s = 13*" "


def count_find_num(primesl: list, limit: int):
    fs = set(primesl)   # factor's set
    rl = [0, 0]         # result list
    nl = []             # number's list

    for i in range(2, limit + 1):
        fsi = calculate_prime_factors(i)[0]
        if fs == fsi:
            rl[0] += 1
            rl[1] = i
            nl.append([i, calculate_prime_factors(i)[1]])

    print("\nResult list:", rl)
    print_numbers_list(nl, limit)

    return rl if rl[0] != 0 else []


# Для проверки:


primesL = [2, 3]
limit = 200
assert count_find_num(primesL, limit) == [13, 192]

primesL = [2, 5]
limit = 200
assert count_find_num(primesL, limit) == [8, 200]

primesL = [2, 3, 5]
limit = 500
assert count_find_num(primesL, limit) == [12, 480]

primesL = [2, 3, 5]
limit = 1000
assert count_find_num(primesL, limit) == [19, 960]

primesL = [2, 3, 47]
limit = 200
assert count_find_num(primesL, limit) == []

primesL = [2, 3, 7]
limit = 200
assert count_find_num(primesL, limit) == [4, 168]

primesL = [2, 5, 7]
limit = 500
assert count_find_num(primesL, limit) == [5, 490]
