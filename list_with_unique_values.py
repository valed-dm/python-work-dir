my_list = []
#
qty = int(input("please, enter list length: "))
for i in range(qty):
    my_list.append(int(input("enter the num " + str(i + 1) + ": ")))

print(my_list)
    
new_list = []
for num in my_list:
    if num in new_list:
        continue
    new_list.append(num)
#
print("The list with unique elements only:")
print(new_list)
