#Driver code for tick-tak-toe
# Note : give input for cordinates with space eg : 0 1 or 1 1

board = [['', '', ''], ['', '', ''], ['', '', '']]

def print_board(board):
    print(*board[0], sep=' | ')
    print("---------------")
    print(*board[1], sep=' | ')
    print("---------------")
    print(*board[2], sep=' | ')
    print("---------------")

def get_marker():
    marker1 = input("Player 1, choose 'X' or 'O': ").upper()
    marker2 = ""
    if marker1 == "X":
        marker2 = "O"
    elif marker1 == "O":
        marker2 = "X"
    else:
        print("Invalid input")
        return get_marker()
    return [marker1, marker2]

def get_coordinates():
    x, y = list(map(int, input("Enter coordinates: ").split()))
    if x in [0, 1, 2] and y in [0, 1, 2]:
        return x, y
    else:
        print("Invalid coordinates")
        return get_coordinates()

def check_win(board):
    for row in board:
        if row[0] == row[1] == row[2] != '':
            return True
    for i in range(len(board)):
        if board[0][i] == board[1][i] == board[2][i] != '':
            return True
    if board[0][0] == board[1][1] == board[2][2] != '':
        return True
    if board[0][2] == board[1][1] == board[2][0] != '':
        return True
    return False

def update_board(board, chance, marker, x, y):
    if chance:
        board[x][y] = marker
        if check_win(board):
            print("Player 1 wins")
            return "game over"
        return False
    else:
        board[x][y] = marker
        if check_win(board):
            print("Player 2 wins")
            return "game over"
        return True

def play_game():
    m1, m2 = get_marker()
    print(f"Player 1: {m1}, Player 2: {m2}")
    chance = True
    while True:
        print_board(board)
        x, y = get_coordinates()
        if chance:
            result = update_board(board, chance, m1, x, y)
            if result == "game over":
                break
            else:
                chance = result
        else:
            result = update_board(board, chance, m2, x, y)
            if result == "game over":
                break
            else:
                chance = result

play_game()
