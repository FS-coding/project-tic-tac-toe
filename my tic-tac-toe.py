from random import choice


def display_board(board):
    global cpu_move
    print(f'+-------+-------+-------+\n|       |       |       |\n|   {board[0][0]}   |   {board[0][1]}   |   {board[0][2]}   |\n|       |       |       |\n+-------+-------+-------+\n|       |       |       |\n|   {board[1][0]}   |   {board[1][1]}   |   {board[1][2]}   |\n|       |       |       |\n+-------+-------+-------+\n|       |       |       |\n|   {board[2][0]}   |   {board[2][1]}   |   {board[2][2]}   |\n|       |       |       |\n+-------+-------+-------+')

    if victory_for(board, cpu_move):
        if cpu_move == False:
            cpu_move = True
            player_move()
        else:
            cpu_move = False
            computer_move()
    return


def player_move():
    move = input("\nEnter your move: ")
    if move not in free:
        print("\nEnter a valid number")
        player_move()

    find_in_board(board, move, 'O')


def computer_move():
    input("Continue with computer move")
    move = choice(free)
    print("My move is: " + move)
    find_in_board(board, move, 'X')


def find_in_board(board, move, play):
    for row in range(3):
        for col in range(3):
            if board[row][col] == move:
                board[row][col] = play
    free.remove(move)
    display_board(board)


def victory_for(board, cpu_move):
    if len(free) == 0:
        print("It's a draw!")
        return False

    if (board[0][0] == board[0][1] == board[0][2] or
       board[1][0] == board[1][1] == board[1][2] or
       board[2][0] == board[2][1] == board[2][2] or
       board[0][0] == board[1][0] == board[2][0] or
       board[0][1] == board[1][1] == board[2][1] or
       board[0][2] == board[1][2] == board[2][2] or
       board[0][0] == board[1][1] == board[2][2] or
       board[0][2] == board[1][1] == board[2][0]):

        if cpu_move == True:
            print("Player wins")
        else:
            print("CPU wins")
        return False
    return True


cpu_move = False

board = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
free = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

display_board(board)
