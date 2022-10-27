def bmi(weight, height):
    if height < 1.0 or height > 2.5 or \
            weight < 20 or weight > 200:
        return None

    return weight / height ** 2


print(bmi(352.5, 1.65))


# take a look at the way the backslash (\) symbol is used. If you use it in Python code and end a line with it, it will tell Python to continue the line of code in the next line of code.


# def lb_to_kg(lb):
#     return lb * 0.45359237

# print("pound to kg", lb_to_kg(1))

# def ft_and_inch_to_m(ft, inch=0.0):
#     return ft * 0.3048 + inch * 0.0254

# print("ft_and_inch_to_m", ft_and_inch_to_m(1))

def ft_and_inch_to_m(ft, inch = 0.0):
    return ft * 0.3048 + inch * 0.0254


def lb_to_kg(lb):
    return lb * 0.45359237


def bmi(weight, height):
    if height < 1.0 or height > 2.5 or weight < 20 or weight > 200:
        return None
    
    return weight / height ** 2


print(bmi(weight = lb_to_kg(176), height = ft_and_inch_to_m(5, 7)))

