# Задача №2.

# Написать метод int32_to_ip, который принимает на вход 32-битное целое число (integer) и
# возвращает строковое представление его в виде IPv4-адреса:

# 2149583361 -> "128.32.10.1"
# 32         -> "0.0.0.32"
# 0          -> "0.0.0.0"

# The integer representation of the IP address:
# (oct1 * 256 ** 3) + (oct2 * 256 ** 2) + (oct3 * 256 ** 1) + (oct4 * 256 ** 0) = decimal
# 192.168.1.34 <==> (((192 * 256 + 168) * 256 + 1) * 256 + 34

# ----------------------------------------------------------------------------
# import ipaddress

# def integer_32_to_ip(int32):
#     print("int32: " + str(int32) + " --> IPv4: " +
#           ipaddress.ip_address(int32).__str__())
#     return ipaddress.ip_address(int32).__str__()

# recursion method int -> binary:
# def decimal_to_binary(num):
#     if num > 0:
#         decimal_to_binary(num//2)
#     print(num % 2, end="")

# def int_to_bin(n):
#     print("\n", bin(n))

# def bin_to_int(n):
#     return int(n,2)
# ----------------------------------------------------------------------------

def ipv4_to_int(ip_str: str):
    decimal = 0
    list_ip = ip_str.split(".")
    list_ip = list(map(lambda x: int(x), list_ip))
    for i in range(4):
        decimal += list_ip[i] * 256 ** (3-i)
    # decimal = list_ip[0] * 256 ** 3 + list_ip[1] * 256 ** 2 + list_ip[2] * 256 + list_ip[3]
    return decimal


# Основа:


def int32_to_ip(int_num: int):
    b = str(bin(int_num))
    b = b[b.find("b") + 1:]
    ip_list = []

    if len(b) < 32:
        b = "0"*(32-len(b)) + b
    elif len(b) > 32:
        print("int_num is greater than 32 bit")
        return

    for i in range(4):
        ip_list.append(b[i*8:(i*8+8)])

    ip_list = list(map(lambda x: str(int(x, 2)), ip_list))

    return ".".join(ip_list)


# Для проверки:

assert int32_to_ip(2154959208) == "128.114.17.104"
assert int32_to_ip(0) == "0.0.0.0"
assert int32_to_ip(2149583361) == "128.32.10.1"
assert int32_to_ip(10) == "0.0.0.10"

print("128.114.17.104 --> int:", ipv4_to_int("128.114.17.104"))
print("192.168.1.34 --> int:", ipv4_to_int("192.168.1.34"))
print("2154959208 --> IPv4:", int32_to_ip(2154959208))
print("3232235810 --> IPv4:", int32_to_ip(3232235810), "\n")

for i in range(11):
    print(10 ** i, "--> IPv4:", int32_to_ip(10 ** i))
