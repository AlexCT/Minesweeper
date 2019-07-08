# Simple Minesweeper Game
# Alex Tresselt, 7-7-19

import random

# Settings
YES = "y"
NO = "n"
MINE = "M"
MIN_MINES = 1
MIN_SIZE = 2
MAX_SIZE = 16
YN_MESSAGE = "Please Enter 'y' for yes or 'n' for no"

# Creates a new blank board, which is a 2D array of size number of size length arrays, with a blank space
# as values. Example for newboard(4):
# [' ', ' ', ' ', ' ']
# [' ', ' ', ' ', ' ']
# [' ', ' ', ' ', ' ']
# [' ', ' ', ' ', ' ']
def newboard(size):
    board = []
    for i in range(size):
        rw = [" "] * size
        board.append(rw)
    return board


# Prints a board with labelled column and row numbers.
# Example:
# X['0', '1', '2', '3']
# 0[' ', ' ', ' ', ' ']
# 1[' ', ' ', ' ', ' ']
# 2[' ', ' ', ' ', ' ']
# 3[' ', ' ', ' ', ' ']
def display(board):
    i = 0
    header = []
    for c in range(len(board)):
        header.append(str(c))
    print("X" + str(header))
    for row in board:
        print(str(i) + str(row))
        i += 1


# Asks player for a number, and ensures it is between the given min and max values.
def inputInt(message, min, max):
    errormessage = "Number must be between " + str(min) + " and " + str(max)
    valid = False
    while(not valid):
        try:
            answer = int(input(message))
        except:
            print(errormessage)
            continue
        if min <= answer <= max:
            valid = True
            return answer
        else:
            print(errormessage)


# Asks player for a yes/no answer, and ensures valid input.
def inputYN(message):
    valid = False
    while not valid:
        try:
            answer = str(input(message))
        except:
            print(YN_MESSAGE)
            continue
        if answer is YES or answer is NO:
            valid = True
            return answer
        else:
            print(YN_MESSAGE)


# Creates a num length set of random (x,y) mine coordinates for a board of the given size.
def plantmines(num, size):
    mines = set()
    while len(mines) < num:
        mines.add((random.randrange(size), random.randrange(size)))
    return mines


# Returns the number of mines in the spaces adjacent to the move.
def adjacentmines(mines, move):
    row = move[0]
    column = move[1]
    count = 0
    for x in range(-1, 2):
        for y in range(-1, 2):
            if (row + x, column + y) in mines:
                count += 1
    return count


# Plays the game.
def play():

    # Create a new board.
    size = inputInt("Enter size of board (" + str(MIN_SIZE) + "-" + str(MAX_SIZE) + "):", MIN_SIZE, MAX_SIZE)
    board = newboard(size)

    # Assign random mine locations.
    maxmines = size * size - 1
    nummines = inputInt("Enter number of mines (" + str(MIN_MINES) + "-" + str(maxmines) + "):", MIN_MINES, maxmines)
    mines = plantmines(nummines, size)

    # Create a set to keep track of player moves.
    moves = set()

    # Display the board.
    display(board)

    # Start playing
    playing = True
    while(playing):

        # Get player's move.
        print("\nEnter move: ")
        column = inputInt("column: ", 0, size - 1)
        row = inputInt("row : ", 0, size - 1)
        move = (row, column)

        # If the player has chosen a mine, game over.
        if (row, column) in mines:
            print("You hit a mine! Game Over!")
            playing = False
        # If the player has already made the same move, restarts the loop to try again.
        elif move in moves:
            print("You have already played that!")
            continue
        # Adds the move to the list of moves, then displays the board with the number of adjacent mines to that space.
        else:
            moves.add(move)
            board[row][column] = str(adjacentmines(mines, move))
            display(board)
        # If the number of player's move is equal to the number of spaces without mines, then there are no more mines
        # left to discover and they have won.
        if len(moves) is (size * size) - nummines:
            print("You win!")
            playing = False

    # Display the location of all the mines on the board.
    for m in mines:
        board[m[0]][m[1]] = MINE
    display(board)

    restart = inputYN("\nWould you like to play again? (y/n)")
    return restart


# Start the game.
def start():

    print("!Welcome to Minesweeper!\n"
          "Instructions: \n"
          "Select all spaces on the board without hitting a mine. The number shown will be amount of mines\n"
          "in the spaces surrounding your choice.\n"
          "       COLUMN   \n"
          "  X['0', '1', '2']\n"
          "R 0['0', '1', '1']\n"
          "O 1['0', '2', 'M']\n"
          "W 2['0', '2', 'M']")

    answer = inputYN("\nStart New Game? (y/n)")
    while answer is YES:
        answer = play()

    print("\nThanks for Playing!")

start()

