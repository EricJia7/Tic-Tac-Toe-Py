
import random
import os
from IPython.display import clear_output

def display_board(board):
    clear_output()
    print '-----|-----|-----'
    print ' ', board[7],'', '|','', board[8],' ' '|'  ,'', board[9]
    print '-----|-----|-----'
    print ' ', board[4],'', '|','', board[5],' ' '|'  ,'', board[6]
    print '-----|-----|-----'
    print ' ', board[1],'', '|','', board[2],' ' '|'  ,'', board[3]
    print '-----|-----|-----'
    print '\n'


def player_input():
    marker = ''
    while (marker != 'X' and marker != 'O'):
        marker = raw_input("Player 1, Do you want to use X or O:  ").upper()
    if marker == 'X':
        return ('X', 'O')
    elif marker == 'O':
        return ('O', 'X')

def place_marker(board, marker, position):
    typein = raw_input("Select a Position:   ")
    a = int(typein)
    while (a > 9):
        print 'Postion out of the board range, please select it again   '
        typein_wrong = raw_input("Select a Position:    ")
        a = int(typein_wrong)
    board[a] = marker
    position = a

def win_check(board,mark):
    if board[1] == board[2] and board[1] == board[3] and board[1] == mark:
        return True
    elif board[4] == board[5] and board[4] == board[6] and board[4] == mark:
        return True 
    elif board[7] == board[8] and board[7] == board[9] and board[7] == mark:
        return True 
    elif board[1] == board[4] and board[1] == board[7] and board[1] == mark:
        return True 
    elif board[2] == board[5] and board[2] == board[8] and board[2] == mark:
        return True 
    elif board[3] == board[6] and board[3] == board[9] and board[3] == mark:
        return True 
    elif board[1] == board[5] and board[1] == board[9] and board[1] == mark:
        return True 
    elif board[3] == board[5] and board[3] == board[7] and board[3] == mark:
        return True 
    else:
        return False

def choose_first():
    if random.random() > 0.5:
        print 'Player 1 Goes First'
        return True
    else:
        print 'Player 2 Goes First'
        return False 

def space_check(board, position):
    #if board[position] == 'O' or board[postion] == 'X':
        #return false
    return board[position] == ''

def full_board_check(board):
    occupy = 0
    for num in board:
        if num == 'X':
            occupy +=1
        elif num == 'O':
            occupy +=1
    if occupy == 9:
        return True
    else:
        return False 

def playher_choice(board):
    
    position = ''
    
    while position not in '1 2 3 4 5 6 7 8 9'.split() or not space_check(board, int(position)):
        position = raw_input('Please choose your position (1-9) ')

def replay():
    replay = raw_input("Do you want to play again? Please type in Y or N: ").upper()
    check = True
    if replay == 'Y':
        return True
    elif replay == 'N':
        return False
    else:
        while check:
            print 'Please type either Y or N'
            replay = raw_input("Do you want to play again? Please type in Y or N: ").upper()
            if replay == 'Y':
                check = False
                return True
            elif replay == 'N':
                check = False
                return False 

print('Welcome to Tic Tac Toe!')

board = [0,1,2,3,4,5,6,7,8,9]  

marker = player_input()

loop = True

test = 0

while loop:
    loop = False
    display_board(board)   
    position = 0
    player_one_first = choose_first()
    while not full_board_check(board):
        if player_one_first == True:
            player_one_first = False
            place_marker(board, marker[0],position)
            display_board(board) 
            print 'Now it is player 2 turn \n'
            if win_check(board,marker[0]):
                print ('Player 1 has won. Game End!')
                break
            elif full_board_check(board):
                print ('Table is full and this is draw!')
            
        elif player_one_first == False:
            player_one_first = True
            place_marker(board,marker[1],position)
            display_board(board)
            print 'Now it is player 1 turn \n'
            if win_check(board,marker[1]):
                print ('Player 2 has won. Game End!')
                break
            elif full_board_check(board):
                print ('Table is full and this is draw!')
    
    if replay() == True:
        loop = True
        board = [0,1,2,3,4,5,6,7,8,9]  
    
    else:
        print '\n Now exit the game, goodbye'
