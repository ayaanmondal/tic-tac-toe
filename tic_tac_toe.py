from array import *

board=['-','-','-',
       '-','-','-',
       '-','-','-'
                  ]
winner = None
game_still_going = True
current_player = "X"

def play_game():

    display_board()

    while game_still_going:

        handle_turn(current_player)

        cheak_if_game_over()

        flip_player()

    if winner == "X" or winner == "O":
        print(winner + ' win the match')
    elif winner == None:
       print("match tie")



def display_board():
    print(board[0] + '|' + board[1] + '|' +board[2])
    print(board[3] + '|' + board[4] + '|' + board[5])
    print(board[6] + '|' + board[7] + '|' + board[8])


def handle_turn(player):
    valid = False
    while not valid:
        print(player + "'s turn")
        position = input("enter a position from 1-9")
        while position not in ["1","2","3","4","5","6","7","8","9"]:
            position = input("invalid error.enter a position from 1-9")

        position = int(position) - 1
        if board[position]=="-":
            valid = True
        else:
            print("you cant go there")


    board[position]=player
    display_board()




def cheak_if_game_over():
    cheak_for_winner()
    cheak_if_tie()

def cheak_for_winner():
    global winner

    row_winner=cheak_row()
    column_winner=cheak_colomn()
    diagonal_winner=cheak_diagonal()
    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None
    return



def cheak_row():
    global game_still_going

    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"
    if row_1 or row_2 or row_3:
        game_still_going = False
    if row_1:
         return board[0]
    elif row_2:
         return board[3]
    elif row_3:
         return board[6]
    return

def cheak_colomn():
    global game_still_going
    colomn_1 = board[0] == board[3] == board[6] != "-"
    colomn_2 = board[1] == board[4] == board[7] != "-"
    colomn_3 = board[3] == board[5] == board[8] != "-"
    if colomn_1 or colomn_2 or colomn_3:
        game_still_going = False
    if colomn_1:
        return board[0]
    elif colomn_2:
        return board[1]
    elif colomn_3:
        return board[3]
    return

def cheak_diagonal():
    global game_still_going
    diagonal_1 = board[0] == board[4] == board[8] != "-"
    diagonal_2 = board[2] == board[4] == board[6] != "-"
    if diagonal_1 or diagonal_2:
        game_still_going = False
    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[2]


    return


def cheak_if_tie():
    global game_still_going
    if "-" not in board:
        game_still_going = False


    return


def flip_player():
    global current_player
    if current_player == "X":
        current_player = "O"

    elif current_player == "O":
        current_player = "X"
    return


play_game()