variable_1 = 1
variable_2 = 2

variable_1, variable_2 = variable_2, variable_1

print(variable_1, variable_2)

my_list = [10, 1, 8, 3, 5]
length = len(my_list)

for i in range(length // 2):
    my_list[i], my_list[length - i - 1] = my_list[length - i - 1], my_list[i]

print(my_list)