import random
from turtle import position
#global variables 
board = ["-", "-" , "-",
         "-", "-" , "-",               
         "-", "-" , "-",]

currentPlayer = "X"
winner = None
gameRunning = True

# printing the game board 
def printBoard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("----------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("----------")
    print(board[6] + " | " + board[7] + " | " + board[8])
#take player input 
def playerInput(board):
    userinput = int(input("Enter a number 1-9: ")) # the reason for int is because python coverts input into a string without it 
    if userinput >= 1 and userinput <= 9 and board[userinput-1] == "-": # checks valid number from 1-9, and at the position that no has gone there 
        board[userinput-1] = currentPlayer # we set the position to current player 
    else: 
        print("Player is already in that spot!")

# check for win or tie 
def checkHorizontal(board):
    global winner
    if board[0] == board[1] == board[2] and board[1] != "-":
        winner = board[0]
        return True 
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winnder = board[3]
        return True 
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[6]
        return True 

def checkRow(board):
    global winner 
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[2]
        return True 

def checkDiagnoal(board):
    global winner 
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True 
    elif board[2] == board[4] == board[6] and board[2] != "-":
        winner = board[2]
        return True 

def checkTie(board):
    if "-" not in board:
        printBoard(board)
        print(" It is a tie!")
        gameRunning = False 

def checkWin():
    if checkDiagnoal(board) or checkHorizontal(board) or checkRow(board):
        print(f"The winner is {winner}")
# swtich the player 
def switchPlayer():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer = "X"
# Computer player
def computer (board):
    while currentPlayer == "O":
        position = random.randint(0,8)
        if board[position] == "-": 
            board[position] = "O"
            switchPlayer()


# check for win or tie again 

while gameRunning:
    printBoard(board) 
    playerInput(board)
    checkWin()
    checkTie(board)
    switchPlayer()
    computer(board)
    checkWin()
    checkTie(board)
