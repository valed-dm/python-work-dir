from decimal import *
getcontext().prec = 3 # 28 default

# unit_price = 2.32
# number_sold = 3
# money_received = 6.96

# print(unit_price * number_sold)

# if unit_price * number_sold == money_received:
#     print('Accounts balanced')
# else:
#     raise ValueError('Accounts not balanced')

с = getcontext()
print(с)

unit_price = Decimal('3.1415')
number_sold = 3
money_received = Decimal('9.42')

print(unit_price * number_sold)

if unit_price * number_sold == money_received:
    print('Accounts balanced')
else:
    raise ValueError('Accounts not balanced')
