# print(1//2) # 0

# print("a","b", "c", sep="sep") #asepbsepc

# foo = (1,2,3)
# foo.index(0) # ValueError: tuple.index(x): x not in tuple

# print(Hello, World!) # outputs Syntax error

# my_list = [1,2]
# for v in range(2):
#     my_list.insert(-1,my_list[v])
# print(my_list) # [1,1,1,2]

# list = [[x for x in range(3)] for y in range(3)] # [[0, 1, 2], [0, 1, 2], [0, 1, 2]]
# for r in range(3):
#     for c in range(3):
#         if list[r][c] % 2 != 0:
#             print("#") # prints three #
# print(0, 1, 2 % 2) -> 0, 1, 0 !!!!!!!

# dct = {}
# dct['1'] = (1,2)
# dct['2'] = (2,1)
# print(dct) # {'1': (1, 2), '2': (2, 1)}

# for x in dct.keys():
#     print(dct[x][1], end="")

# try:
#     print(5/0)
#     # break # SyntaxError: 'break' outside loop
# except:
#     print("Sorry, something went wrong ...") # SyntaxError: default 'except:' must be last
# except (ValueError, ZeroDivisionError):
#     print("Too bad ...")

# dd = {"1" : "0", "0" : "1 "}
# for x in dd.vals(): # AttributeError: 'dict' object has no attribute 'vals'. Did you mean: 'values'?
#     print(x, end="")

# my_list = [x * x for x in range(5)] # [0, 1, 4, 9, 16]
# def fun(lst):
#     del lst[lst[2]]
#     return lst

# print(fun(my_list)) # [0, 1, 4, 9]