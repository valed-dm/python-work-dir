# no user_data input validation done yet - this fact has no effect on main code logic

# sb = sudoku_board
sb = [[0 for i in range(9)] for j in range(9)]

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
        # sudoku string unique sum
        if sum == 45:
            strngs = True
        else:
            strngs = False
            break

    for i in range(9):
        sum = 0
        for j in range(9):
            sum += sb[j][i]
        # sudoku column unique sum
        if sum == 45:
            clmns = True
        else:
            clmns = False
            break
    # sudoku square unique sum vars initialization
    sq1 = sq2 = sq3 = sq4 = sq5 = sq6 = sq7 = sq8 = sq9 = 0
    # squares sum calculation
    for i in range(3):
        sq1 += (sb[0][i] + sb[1][i] + sb[2][i])
        sq2 += (sb[0][i+3] + sb[1][i+3] + sb[2][i+3])
        sq3 += (sb[0][i+6] + sb[1][i+6] + sb[2][i+6])
        sq4 += (sb[3][i] + sb[4][i] + sb[5][i])
        sq5 += (sb[3][i+3] + sb[4][i+3] + sb[5][i+3])
        sq6 += (sb[3][i+6] + sb[4][i+6] + sb[5][i+6])
        sq7 += (sb[6][i] + sb[7][i] + sb[8][i])
        sq8 += (sb[6][i+3] + sb[7][i+3] + sb[8][i+3])
        sq9 += (sb[6][i+6] + sb[7][i+6] + sb[8][i+6])

    if sq1 == sq2 == sq3 == sq4 == sq5 == sq6 == sq7 == sq8 == sq9 == 45:
        sqrs = True

    if strngs and clmns and sqrs:
        print("Yes!")
    else:
        print("No!")

    print("strngs", strngs)
    print("clmns", clmns)
    print("sqrs", sqrs)


sudoku_test(sb)

# Sample input: 295743861 431865927 876192543 387459216 612387495 549216738 763524189 928671354 154938672
# Sample input: 195743862 431865927 876192543 387459216 612387495 549216738 763524189 928671354 254938671

# Your task is to write a program which:

# reads 9 rows of the Sudoku, each containing 9 digits (check carefully if the data entered are valid)
# outputs Yes if the Sudoku is valid, and No otherwise.
