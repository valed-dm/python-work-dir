# Copying the entire list.
list_1 = [1]
list_2 = list_1[:]
list_1[0] = 2
print(list_2)

# Copying some part of the list. my_list[start:end]
my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:3]
print(new_list)

# This is how negative indices work with the slice:
my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:-1]
print(new_list)

# If the start specifies an element lying further than the one described by the end (from the list's beginning point of view), the slice will be empty:

my_list = [10, 8, 6, 4, 2]
new_list = my_list[-1:1]
print(new_list)

my_list = [10, 8, 6, 4, 2]
new_list = my_list[:3]
print(new_list)

my_list = [10, 8, 6, 4, 2]
new_list = my_list[3:]
print(new_list)

# omitting both start and end makes a copy of the whole list:
my_list = [10, 8, 6, 4, 2]
new_list = my_list[:]
print(new_list)

my_list = [10, 8, 6, 4, 2]
del my_list[1:3]
print(my_list)

# The list becomes empty, and the output is: [].
my_list = [10, 8, 6, 4, 2]
del my_list[:]
print(my_list)

# Removing the slice from the code changes its meaning dramatically. Error
my_list = [10, 8, 6, 4, 2]
del my_list
print(my_list)
