##############################
#
# Names: Lily Davisson and Mia McDuffie
# Description
'''
This is a very simple tic tac toe game where two people play against each other.
We chose this game because it tests our understanding with lists, for loops, and while loops.
One the game is initialized the players get to choose there name and symbol. From there,
the players play a game until one of them win or until there are no more moves.
Once that happens, the players are asked if they want to play again and if they want to change there symbols.
'''
##############################

import random
import time

def tictactoe():
    '''
    Initialize tic-tac-toe
    '''
    print('Welcome to Tic Tac Toe!')
    print()
    #Sets up the name and the marker for player one
    print("Hello player one. What would you like to be called?")
    player1name = str(input(": "))
    print(player1name + ", which letter/symbol would you like to use as your tic-tac-toe marker? ")
    onesymbol = input(": ")
    while not check_marker(onesymbol, None, None):  #checks if the marker input is valid
        print("Which letter would you like to use? ")
        onesymbol = input(": ")
    #Sets up the name and the marker for player two
    print("\nHello player two. What would you like to be called?")
    player2name = input(": ")
    print(player2name + ", which letter/symbol would you like to use as your tic-tac-toe marker? ")
    twosymbol = input(": ")
    while not check_marker(twosymbol, onesymbol, player1name):  #checks if the marker input is valid
        print("Which letter would you like to use? ")
        twosymbol = input(": ")

    while True:
        #starts the main game
        onegame(player1name, player2name, onesymbol, twosymbol)
        #aks if the player wants to play again
        print("Would you like to play again? (yes/no)")
        answer1 = input(": ").lower()
        if answer1 == "yes" or answer1 == "y":  #starts a new game if yes
            print("Would you like to choose new names/markers? (yes/no)")
            answer2 = input(": ").lower()
            if answer2 == "yes" or answer2 == "y":
                tictactoe()
        else:   #ends the game if no
            break

def onegame(player1name, player2name, onesymbol, twosymbol):
    '''
    (str, str, str, str) -> None
    play one game of tic-tac-toe.
    '''
    row1 = ["_","_","_"]
    row2 = ["_","_","_"]
    row3 = ["_","_","_"]
    rows = [row1, row2, row3]

    print("\nOkay, I'll roll a dice to see who goes first.")
    time.sleep(1)
    print("...")
    #sets up who is going to go first
    first = random.randint(1, 2)

    if first == 1:
        print()
        print(player1name, "is going first.") #Player 1 goes first

        while True: #calls on one move for Player 1 and 2
            if onemove(player1name, onesymbol, rows, twosymbol) == True:
                break
            if onemove(player2name, twosymbol, rows, onesymbol) == True:
                break
    else:
        print(player2name, "is going first.") #Player 2 goes first
        while True: #calls on one move for Player 1 and 2
            if onemove(player2name, twosymbol, rows, onesymbol) == True:
                break
            if onemove(player1name, onesymbol, rows, twosymbol) == True:
                break

def onemove(name, symbol, rows, symbol_2):
    '''
    (str, str, list, list, list) -> Bool
    Ask for one move, validate the input and assign that move to the board.
    '''
    #prints the cordinates of the board
    print("\nCurrent board: \n", ' '.join(rows[0]), "    1,1 1,2 1,3\n", ' '.join(rows[1]), "    2,1 2,2 2,3\n", ' '.join(rows[2]), "    3,1 3,2 3,3\n") # print current board and the corresponding numbers
    #aks where does the player want to play
    print(name + ", which space would you like to play? (Enter value combination shown. Ex: 1,2 for top left, 2,2 for middle, 3,3 for bottom right)")
    move = input(': ') # ask user for move
    location = locate_move(move, rows)
    while location == False or check_move(location) == False: #keeps asking for the cordinate until a valid one is given
        print(name + ", which space would you like to play? ")
        move = input(": ")
        location = locate_move(move, rows)
    location[0][location[1]] = symbol
    if check_winner(symbol, rows): #checks if there is a winner
        print("\nCurrent board: \n", ' '.join(rows[0]), "\n", ' '.join(rows[1]), "\n", ' '.join(rows[2]), "\n") # print current board and the corresponding numbers
        print()
        print(name, "wins!") #prints the winners name and returns True to onegame function
        return True
    if check_if_win_possible(symbol, rows, symbol_2):
        print("\nCurrent board: \n", ' '.join(rows[0]), "\n", ' '.join(rows[1]), "\n", ' '.join(rows[2]), "\n")
        print()
        print('Sorry, no one won!')
        return True

def check_marker(value, previous, name):
    '''
    (str) -> Bool
    Validate input of marker character. Cannot be number or more than one character.
    '''
    if value in ["_"," _ "," "] or value.isdigit() or len(value) != 1: #checks is the markers is valid
        print()
        print("Please enter a single letter to use as your marker.")
        return False
    if value == previous: #Checks is the name given is the same
        print()
        print("Oops,", name, "already chose this marker. Please choose another.")
        return False
    return True #returns True is marker is valid

def locate_move(move, rows):
    '''
    (str, list, list, list) -> Bool or (row#, index of move)
    Returns location of move as (row, index number).
    If incorrect move format is entered, return False.
    '''
    #checks if move in the coordinates
    if len(move) != 3 or move not in ["1,1", "1,2", "1,3", "2,1", "2,2", "2,3", "3,1", "3,2", "3,3"]:
        print()
        print("Please enter a valid number combination. See which combination (Ex: 1,1, 1,3, 2,1) corresponds to which space next to the current board.")
        return False
    #if is a correct move then assign the row and index of the move
    move = move.strip().split(",")
    for i in range(2):
        move[i] = int(move[i])
    for value in move: # change str into int to index with
        value = int(value)
    if move[0] == 1: # row 1
        return (rows[0], (move[1]-1))
    elif move[0] == 2: # row 2
        return (rows[1], (move[1]-1))
    elif move[0] == 3: # row 3
        return (rows[2], (move[1]-1))

def check_move(location):
    '''
    ((row, index)) -> Bool
    Make sure move selected is not occupied
    if occupied, return False
    '''
    if location[0][location[1]] != "_":
        print()
        print("This space is occupied, please choose another.")
        return False

def check_winner(symbol, rows):
    '''
    (str, list, list, list) -> Bool
    Check for a win after the last move horizontally for all rows, vertically for all columns, and diagonally starting from the top left corner and
    the bottom left corner.
    '''
    for row in rows: # check for win horizontally
        counter = 0
        for value in row:
            if value == symbol:
                counter += 1
        if counter == 3:
            return True
    for column in range(3): #check for win vertically
        counter = 0
        for row in rows:
            if row[column] == symbol:
                counter += 1
        if counter == 3:
            return True
    # check for win diagonally from top left
    counter = 0
    for indx in range(3):
        if rows[indx][indx] == symbol: # check first value in first row, second value in second row, third value in third row
            counter += 1
    if counter == 3:
        return True
    counter = 0
    start = 2
    for indx in range(3): # check for winner diagonally from top right
        if rows[indx][start-indx] == symbol:
            counter += 1
    if counter == 3:
        return True

def check_if_win_possible(symbol, rows, symbol_2):
    '''
    (str, list, list, list, str) -> Bool
    Goes through each row too see if filled. If all are filled, then return True.
    '''
    all_in = True

    for row in rows:
        for item in row:
            if symbol == item or symbol_2 == item:
                all_in = True
            else:
                all_in = False
                return all_in
    return all_in

tictactoe() #starts the main function
