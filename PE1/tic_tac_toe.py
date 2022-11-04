from random import randrange

board = [[1, 2, 3], [4, "X", 6], [7, 8, 9]]
fields = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
free_fields = [1, 2, 3, 4, 6, 7, 8, 9]
win_combination = []
user_error = False
winner = ""


def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    hor_line = ("+" + 7*"-")*3 + "+"
    ver_line = ("|" + 7*" ")*3 + "|"
    game_lines = {0: "|", 1: "|", 2: "|"}

    for i in range(3):
        for j in range(3):
            game_lines[i] += 3*" " + str(board[i][j]) + 3*" " + "|"

    game_board = {2: game_lines[0], 6: game_lines[1], 10: game_lines[2]}
    for i in range(13):
        if i in [0, 4, 8, 12]:
            game_board[i] = hor_line
        if i in [1, 3, 5, 7, 9, 11]:
            game_board[i] = ver_line

    for i in range(13):
        print(game_board[i])


def user_move(board):
    # The function accepts the board's current status, asks the user about their move,
    # checks the input, and updates the board according to the user's decision.
    global user_error

    try:
        move_to = ""
        for i in range(len(free_fields)):
            if i < len(free_fields) - 1:
                move_to += str(free_fields[i]) + ","
            else:
                move_to += str(free_fields[i]) + ": "

        while True:
            user_move = input("Choose your move: " + move_to)
            if type(int(user_move)) == int:
                user_move = int(user_move)
                break
            else:
                continue

        print("your move:", user_move)

        if user_move < 1 or user_move > 9:
            raise ValueError
        if user_move in free_fields:
            for i in range(len(free_fields)):
                if free_fields[i] == user_move:
                    del free_fields[i]
                    break
        else:
            raise ValueError

        for i in range(3):
            for j in range(3):
                if board[i][j] == user_move:
                    board[i][j] = "O"
                    user_error = False
                    break

    except ValueError:
        user_error = True
        print("You've entered " + str(user_move) +
              ". Please, enter a valid number.")


def computer_move(board):
    # The function accepts the board's current status
    # and randomly updates the board with "X" executing computer move.
    if len(free_fields) == 1:
        random = 0
    elif len(free_fields) > 1:
        random = randrange(len(free_fields) - 1)

    computer_move = free_fields[random]
    del free_fields[random]

    print("computer move:", computer_move)

    for i in range(3):
        for j in range(3):
            if board[i][j] == computer_move:
                board[i][j] = "X"
                break


def victory_for(board, sign):
    # The function analyzes the board's status in order to check if
    # the player using 'O's or 'X's has won the game
    global winner
    global win_combination

    # horizontal lines
    for i in range(3):
        win_count = 0
        for j in range(3):
            if board[i][j] == sign:
                win_count += 1
                if win_count == 3:
                    winner = sign
                    win_combination = [fields[i][0],
                                       fields[i][1], fields[i][2]]
                    break
    # vertical lines
    for i in range(3):
        win_count = 0
        for j in range(3):
            if board[j][i] == sign:
                win_count += 1
                if win_count == 3:
                    winner = sign
                    win_combination = [fields[0][i],
                                       fields[1][i], fields[2][i]]
                    break
    # diagonal 1-5-9 (0,0; 1,1; 2,2)
    for i in range(1):
        win_count = 0
        for j in range(3):
            if board[j][j] == sign:
                win_count += 1
                if win_count == 3:
                    winner = sign
                    win_combination = [1, 5, 9]
                    break
    # diagonal 7-5-3 (2,0; 1,1; 0,2)
    for i in range(1):
        win_count = 0
        for j in range(3):
            if board[2-j][j] == sign:
                win_count += 1
                if win_count == 3:
                    winner = sign
                    win_combination = [7, 5, 3]
                    break


while len(free_fields) > 0:
    display_board(board)
    user_move(board)
    if user_error:
        continue
    if len(free_fields) <= 4:
        victory_for(board, "O")
        if winner == "O":
            break
    computer_move(board)
    if len(free_fields) <= 4:
        victory_for(board, "X")
        if winner == "X":
            break

if len(winner) == 0:
    print("It's a draw")
elif winner == "O":
    print("You won! Win combination: ", win_combination)
elif winner == "X":
    print("Computer won! Win combination: ", win_combination)

print("Final board:")
display_board(board)
