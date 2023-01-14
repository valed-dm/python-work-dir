# Задача №4.

# Написать метод bananas, который принимает на вход строку
# и возвращает количество слов «banana» в строке.

# (Используйте "-" для обозначения зачеркнутой буквы)

# Input: bbananana

# Output:

# b-anana--
# b-anan--a
# b-ana--na
# b-an--ana
# b-a--nana
# b---anana
# -banana--
# -banan--a
# -bana--na
# -ban--ana
# -ba--nana
# -b--anana

# Основа:

# def bananas(s) -> set:
#     result = set()
#     # Your code here!
#     return result


from itertools import combinations


def make_res(tup, s_len):
    res_tup = ["-" for i in range(s_len)]
    for i in range(len(tup)):
        res_tup.pop(int(tup[i][0]))
        res_tup.insert(int(tup[i][0]), tup[i][1])

    return "".join(res_tup)


def bananas(s) -> set:
    result = set()
    w = list("banana")
    s = list(s)
    s = [str(i) + str(el) for i, el in enumerate(s)]
    cmb = list(combinations(s, len(w)))

    for cmb_tup in cmb:
        hits = 0
        for i in range(len(w)):
            if cmb_tup[i][1] == w[i]:
                hits += 1
        if hits == len(w):
            result.add(make_res(cmb_tup, len(s)))

    print(result)

    return result


# Для проверки:
assert bananas("banann") == set()
assert bananas("banana") == {"banana"}
assert bananas("bbananana") == {"b-an--ana", "-banana--", "-b--anana", "b-a--nana", "-banan--a",
                                "b-ana--na", "b---anana", "-bana--na", "-ba--nana", "b-anan--a",
                                "-ban--ana", "b-anana--"}
assert bananas("bananaaa") == {"banan-a-", "banana--", "banan--a"}
assert bananas("bananana") == {"ban--ana", "ba--nana",
                               "bana--na", "b--anana", "banana--", "banan--a"}
