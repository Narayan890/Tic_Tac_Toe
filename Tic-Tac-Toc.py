import random
#from IPython.display import clear_output
def firstTurn():
    turn = random.randint(0,1)
    return turn
def displayBoard(game):
    # Display the board to user
    #clear_output()
    print('\t' + game[1] + '\t' + '|' + '\t' + game[2] + '\t' + '|' + '\t' + game[3])
    print('\t' + '-----------------' + '\t')
    print('\t' + game[4] + '\t' + '|' + '\t' + game[5] + '\t' + '|' + '\t' + game[6])
    print('\t' + '-----------------' + '\t')
    print('\t' + game[7] + '\t' + '|' + '\t' + game[8] + '\t' + '|' + '\t' + game[9])

def playerMark():
    # Outpput = (Player1 marker, Player2 marker)
    check = True
    while check:
        # Getting the marker of user choice
        choice = input("Player 1 choose your Mark X or O :")
        if choice == 'X':
            check = False
            return ('X','O')
        elif choice == 'O':
            check = False
            return ('O','X')
        else:
            check = True

def spaceCheck(game,position):
    # check for space in board
    return game[position] == ''

def fullBoard(game):
    for i in range(1,10):
        # check that any space in board is left or not
        if spaceCheck(game,i):
            return False
    # When board is full
    return True

def gettingPosition():
    check = True
    while True:
        position = int(input('Enter the Position 1 to 9:'))
        if position in [1,2,3,4,5,6,7,8,9]:
            return position
            break
        else :
            print('Please enter a valid position')

def insertValue(game,mark,position):
    if(game[position] == ''):
           game[position] = mark
           return game
    else:
        print('Position is already filled')
        return game




def replay():
    check = input('Do you want to play again ? Y or N :')
    return check == 'Y'

def checkWinner(game,mark):
     if (game[1] == game[2] == game[3] == mark) or (game[4] == game[5] == game[6] == mark) or (game[7] == game[8] == game[9] == mark) :
          return True
     elif (game[1] == game[4] == game[7] == mark) or (game[2] == game[5] == game[8] == mark) or (game[3] == game[6] == game[9] == mark) :
         return True
     elif (game[1] == game[5] == game[9] == mark) or (game[3] == game[5] == game[7] == mark):
         return True
     else :
         return False

print('Welcome to Tic Tac Toe!')

while True:
    game = ['']*10
    Player1mark, Player2mark = playerMark()
    turn = firstTurn()
    if(turn == 1):
        print('Player 1 will go first')
    else:
        print('Player 2 will go first')

    gameon = True
    while gameon:
     if turn == 1:
         # Player 1 turn
        # show the board
        displayBoard(game)
        print('Player 1 turn')
        # choose the position
        position = gettingPosition()

        # place the marker at th position
        game = insertValue(game,Player1mark,position)

        # win check
        if checkWinner(game,Player1mark):
            displayBoard(game)
            print('Player 1 has Won !')
            gameon = False
        else :
            # check if game is tie
            if fullBoard(game):
                displayBoard(game)
                print('Tie game !')
                break
            else:
                turn = 0;

     else:
        # Player 2 turn
        # show the board
        displayBoard(game)
        print('Player 2 turn')
        # choose the position
        position = gettingPosition()

        # place the marker at th position
        game = insertValue(game,Player2mark,position)

        # win check
        if checkWinner(game,Player2mark):
            displayBoard(game)
            print('Player 2 has Won !')
            gameon = False
        else:
            # check if game is tie
            if fullBoard(game):
                displayBoard(game)
                print('Tie game !')
                break
            else:
                turn = 1;

    if not replay():
        print('Thank you for playing!')
        break


