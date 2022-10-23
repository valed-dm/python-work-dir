def is_prime(num):
    count = 0
    for i in range(num):
        if num % (i + 1) == 0:
            count += 1
        if count == 2 and i < (num - 1):
            return False
    return True


for i in range(1, 100):
    if is_prime(i + 1):
        print(i + 1, end=" ")

#prime_num_test = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
