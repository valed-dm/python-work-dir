# 2.3.1.18 Your own split

def mysplit(strng):
    counter = 0
    lngth = len(strng)
    word = ""
    res_list = []
    for ch in strng:
        counter += 1
        if ch != " " and counter != lngth:
            word += ch
        elif ch != " " and counter == lngth:
            word += ch
            res_list.append(word)
        elif len(word) != 0:
            res_list.append(word)
            word = ""

    return res_list



print(mysplit("To be, or not to be, that is the question: Whether 'tis nobler in the mind to suffer"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))