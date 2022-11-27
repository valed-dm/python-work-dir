digits_list = [
    ["****", "*  *", "*  *", "*  *", "****"],
    ["   *", "   *", "   *", "   *", "   *"],
    ["****", "   *", "****", "*   ", "****"],
    ["****", "   *", "****", "   *", "****"],
    ["*  *", "*  *", "****", "   *", "   *"],
    ["****", "*   ", "****", "   *", '****'],
    ["****", "*   ", "****", "*  *", "****"],
    ["****", "   *", "   *", "   *", "   *"],
    ["****", "*  *", "****", "*  *", "****"],
    ["****", "*  *", "****", "   *", "****"]
]
num_list = []

user_input = input("please, enter integer number: ")

for char_num in user_input:
    num_list.append(int(char_num))


def display_num(num):
    str1 = str2 = str3 = str4 = str5 = ""

    for i in range(len(num)):
        str1 += digits_list[num[i]][0] + "  "
        str2 += digits_list[num[i]][1] + "  "
        str3 += digits_list[num[i]][2] + "  "
        str4 += digits_list[num[i]][3] + "  "
        str5 += digits_list[num[i]][4] + "  "

    print(str1 + "\n" + str2 + "\n" + str3 + "\n" + str4 + "\n" + str5)


display_num(num_list)
