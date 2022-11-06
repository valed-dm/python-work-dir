####################
i = 0
while i <= 5:
    i += 1
    if i % 2 == 0:
        break
    print("*")
print(3 % 2)
####################
my_list = [1, 2, 3, 4, 5]
for v in range(len(my_list)):
    my_list.insert(1, my_list[v])
print("my_list: ", my_list)
####################
nums = [1, 2, 3]
vals = nums[-1:-2]
print("vals", vals)
####################
i = 0
while i <= 3:
    i += 2
    print("*")
####################
my_list_1 = [1, 2, 3]
my_list_2 = []
for v in my_list_1:
    my_list_2.insert(0, v)
print(my_list_2)
####################
my_list = [1, 2, 3, 4]
print(my_list[-3:-2])
####################
my_list = [i for i in range(-10, 2)]
print(my_list)
####################
a = 1
b = 0
с = a & b
d = a | b
e = a ^ b
print(с + d + e)
####################

# def fun(in=2, out=3): code is erroneous
#     return in * out

# print("fun function", fun(3))