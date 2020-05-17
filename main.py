# Game of tic tac toe

#--Global Variables--#

# Game Board
board = ["-","-","-",
         "-","-","-",
         "-","-","-"]

# IF game is still going
game_still_going = True

# Who won? or Tie?
winner = None

# Whose turn is it
current_player = "X"

def display_board():
    print(board[0]+" | "+board[1]+" | "+board[2])
    print(board[3]+" | "+board[4]+" | "+board[5])
    print(board[6]+" | "+board[7]+" | "+board[8])


def play_game():    
    # Display initial board
    display_board()

    # While the game is still going
    while game_still_going:
        # Handle a single turn of a player
        handle_turn(current_player)
        
        # Check if the games has ended
        check_if_game_over()
        
        # Flip to the other player
        flip_player()
    
    # The game has ended
    if winner == "X" or winner == "O":
        print (winner + " won.")
    elif winner == None:
        print ("Tie.")

# Handle a single turn of a player
def handle_turn(player):
    print(player + "'s turn.")
    position = input("Choose a position from 1-9: ")

    valid = False

    while not valid:

        # checks the postion is in the valid list until a correct postion is entered
        while position not in ["1","2","3","4","5","6","7","8","9"]:
            position = input("Invalid input. Choose a position from 1-9: ")

        position = int(position) - 1

        if board[position] == "-":
            valid = True
        else:
            print("You can't go there. Go again.")

    board[position] = player
    display_board()


def check_if_game_over():
    check_for_winner()
    check_if_tie()

def check_for_winner():

    #Set up global variable
    global winner
    # check rows
    row_winner = check_rows()
    # check columns
    column_winner = check_columns()
    # check diagonals
    diagonal_winner = check_diagonals()

    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None
    return

def check_rows():
    # Setup global variables
    global game_still_going
    # Check if any of the rows have all the same values and its not empty
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"

    # If any row has a match, flag that there is a win
    if row_1 or row_2 or row_3:
        game_still_going = False
    
    #Return the winner X or O
    if row_1:
        return board[0]
    if row_2:
        return board[3]
    if row_3:
        return board[6]

    return

def check_columns():
    # Setup global variables
    global game_still_going
    # Check if any of the columns have all the same values and its not empty
    col_1 = board[0] == board[3] == board[6] != "-"
    col_2 = board[1] == board[4] == board[7] != "-"
    col_3 = board[2] == board[5] == board[8] != "-"

    # If any column has a match, flag that there is a win
    if col_1 or col_2 or col_3:
        game_still_going = False
    
    #Return the winner X or O
    if col_1:
        return board[0]
    if col_2:
        return board[1]
    if col_3:
        return board[2]
    return

def check_diagonals():
    # Setup global variables
    global game_still_going
    # Check if any of the diagonals have all the same values and its not empty
    diagonal_1 = board[0] == board[4] == board[8] != "-"
    diagonal_2 = board[2] == board[4] == board[6] != "-"

    # If any diagonals has a match, flag that there is a win
    if diagonal_1 or diagonal_2:
        game_still_going = False
    
    #Return the winner X or O
    if diagonal_1:
        return board[4]
    if diagonal_2:
        return board[4]    
    return


def check_if_tie():
    global game_still_going
    if "-" not in board:
        game_still_going = False
    return

def flip_player():
    # Global variables we need
    global current_player
    #if the current player is X then change the player to O
    if current_player == "X":
        current_player = "O"
    #If the current player is O then change the player to X
    elif current_player == "O":
        current_player = "X"
    return


# Call the function
play_game()


# board
# display board
# play game
# handle turn
# check win
    # check rows
    # check columns
    # check diagonals
# check tie
# flip player