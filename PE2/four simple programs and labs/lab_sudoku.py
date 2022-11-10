# no user_data input validation done yet - this fact has no effect on main code logic

sb = [[0 for i in range(9)] for j in range(9)] # sb = sudoku_board

user_data = input("sudoku string: ").replace(" ", "")

for i in range(9):
    for j in range(9):
        sb[i][j] = int(user_data[i*9 + j])

def sudoku_test(sb):
    strngs = False
    clmns = False
    sqrs = False
    
    for i in range(9):
        sum = 0
        for j in range(9):
            sum += sb[i][j]

        if sum == 45:
            strngs = True
        else:
            strngs = False
            break
    
    for i in range(9):
        sum = 0
        for j in range(9):
            sum += sb[j][i]

        if sum == 45:
            clmns = True
        else:
            clmns = False
            break

    sum_sq1 = sum_sq2 = sum_sq3 = sum_sq4 = sum_sq5 = sum_sq6 = sum_sq7 = sum_sq8 = sum_sq9 = 0
   
    for i in range(3):
        sum_sq1 += (sb[0][i] + sb[1][i] + sb[2][i])
        sum_sq2 += (sb[0][i+3] + sb[1][i+3] + sb[2][i+3])
        sum_sq3 += (sb[0][i+6] + sb[1][i+6] + sb[2][i+6])
        sum_sq4 += (sb[3][i] + sb[4][i] + sb[5][i])
        sum_sq5 += (sb[3][i+3] + sb[4][i+3] + sb[5][i+3])
        sum_sq6 += (sb[3][i+6] + sb[4][i+6] + sb[5][i+6])
        sum_sq7 += (sb[6][i] + sb[7][i] + sb[8][i])
        sum_sq8 += (sb[6][i+3] + sb[7][i+3] + sb[8][i+3])
        sum_sq9 += (sb[6][i+6] + sb[7][i+6] + sb[8][i+6])
    
    if sum_sq1 == sum_sq2 == sum_sq3 == sum_sq4 == sum_sq5 == sum_sq6 == sum_sq7 == sum_sq8 == sum_sq9 == 45:
       sqrs = True 
    
    if strngs and clmns and sqrs:
        print("Yes!")
    else:
        print("No!")

    # print("strngs", strngs)
    # print("clmns", clmns)
    # print("sqrs", sqrs)

sudoku_test(sb)

# Sample input: 295743861 431865927 876192543 387459216 612387495 549216738 763524189 928671354 154938672
# Sample input: 195743862 431865927 876192543 387459216 612387495 549216738 763524189 928671354 254938671