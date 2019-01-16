from IPython.display import clear_output

import random

def choose_first():
    call = ''
    while call.lower() != 'heads' and call.lower() != 'tails':
        call = input('Player 1, choose heads or tails: ')
    
    first = 0
    second = 0
    coin = random.randint(0,1)
    if coin == 0 and call == 'heads':
        print('The coin is tails. Player 2 goes first.')
        first = 2
        second = 1
    elif coin == 0 and call == 'tails':
        print('The coin is tails. Player 1 goes first.')
        first = 1
        second = 2
    elif coin == 1 and call == 'heads':
        print('The coin is heads. Player 1 goes first.')
        first = 1
        second = 2
    elif coin == 1 and call == 'tails':
        print('The coin is heads. Player 2 goes first.')
        first = 2
        second = 1
        
    return (first, second)

def player_input(order):
    first = order[0]
    marker = ''
    # KEEP ASKING FIRST PLAYER TO CHOOSE X OR O
    while marker != 'X' and marker != 'O':
        marker = input(f'Player {first}, choose X or O: ').upper()
    
    # ASSIGN SECOND PLAYER THE OPPOSITE MARKER
    if first == 1:    
        player1 = marker
        if player1 == 'X':
            player2 = 'O'
        else:
            player2 = 'X'
    
    else:
        player2 = marker
        if player2 == 'X':
            player1 = 'O'
        else:
            player1 = 'X'
    
    return (player1, player2)

def display_board(board):
    clear_output()
    print(' '+board[7]+' | '+board[8]+' | '+board[9])
    print('---|---|---')
    print(' '+board[4]+' | '+board[5]+' | '+board[6])
    print('---|---|---')
    print(' '+board[1]+' | '+board[2]+' | '+board[3]) 
    
def player_choice(order, board):
    position = 0
    while position > 9 or position < 1 or not space_check(board, position):
        position = int(input(f'Player {order}, choose a position between 1 and 9: '))
    return position

def space_check(board, position):
    return board[position] != 'X' and board[position] != 'O'

def place_marker(board, marker, position):
    board[position] = marker

def win_check(board, mark):
    if board[1] == board[2] and board[2] == board[3] and board [1] == mark:
        won = True
    elif board[1] == board[5] and board[5] == board [9] and board [1] == mark:
        won = True
    elif board[1] == board[4] and board[4] == board [7] and board [1] == mark:
        won = True
    elif board[2] == board[5] and board[5] == board [8] and board [2] == mark:
        won = True
    elif board[3] == board[6] and board[6] == board [9] and board [3] == mark:
        won = True
    elif board[4] == board[5] and board[5] == board [6] and board [4] == mark:
        won = True
    elif board[7] == board[8] and board[8] == board [9] and board [7] == mark:
        won = True
    elif board[7] == board[5] and board[5] == board [3] and board [7] == mark:
        won = True
    else:
        won = False
    return won

def full_board_check(board):
    full = True
    for i in board:
        if i != 'X' and i != 'O':
            full = False
    return full

def replay():
    again = input('Play again? Y/N: ')      
    if again[0].lower() == 'y':
        return True
    elif again[0].lower() == 'n':
        return False

print('Welcome to Tic Tac Toe!')

while True:
    # Set the game up here
    play_game = input('Are you ready to play? Y/N: ')
    
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False
        
    board = ['X','1','2','3','4','5','6','7','8','9'] 
    order = choose_first()
    marker = player_input(order)
    turn = order[0]

    while game_on:
        
        if turn == 1:
            #First Player's Turn
            display_board(board)
            position = player_choice(1, board)
            place_marker(board, marker[0], position)
       
            if win_check(board, marker[0]):
                display_board(board)
                print(f'Congratulations Player {order[0]}! You won!')
                game_on = False
            else:
                if full_board_check(board):
                    display_board(board)
                    print('The game is a draw...')
                    break
                else:
                    turn = 2
        
        else:
            #Second Player's Turn
        
            display_board(board)
            position = player_choice(2, board)
            place_marker(board, marker[1], position)
        
            if win_check(board, marker[1]):
                display_board(board)
                print(f'Congratulations Player {order[1]}! You won!')
                game_on = False
            else:
                if full_board_check(board):
                    display_board(board)
                    print('The game is a draw...')
                    break
                else:
                    turn = 1
    
    if not replay():
        break
