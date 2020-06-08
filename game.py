from util import *
from agent import *

# grid is 3x3
# 1 goes first
# 0 is unoccupied, 1 and 2 are players
# 
# This is the main module integrating all the components


V = True

def player_handle_move(grid, player):
    print("Grid is currently:")
    showGrid(grid)
    print("Player " + str(player) + " to move.")
    print("\n")
    while True:
        print("Select a row (0, 1, or 2)")
        i = int(raw_input()) # No room for user error
        print("Select a column (0, 1, or 2)")
        j = int(raw_input())
        box = (i, j)
        if moveIsValid(grid, box):
            break
        print("Sorry, move not available, select another move.\n\n")
    return move(grid, player, box) 

def computer_handle_move(grid, player, verbose=V):
    print("Computer's turn.")
    choice = agent_move(player, grid, verbose=verbose) 
    return choice

def game(mode, seed = True):
    global lastChoice
    if seed:
        np.random.seed(12)
    if mode == 4:
        print("Not yet implemented")
        return None
    grid = np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
    r = result(grid)
    while r == 0:
        player = turn(grid)
        if (mode == 1) or ((mode == 2) and (player == 1)) or ((mode == 3) and (player == 2)):
            grid = player_handle_move(grid, player)
        else:
            grid = computer_handle_move(grid, player)
        r = result(grid)
    print("\n\nFinal position:")
    showGrid(grid)
    if mode == 2:
        end_of_game(2, grid, verbose=V) 
    if mode == 3:
        end_of_game(1, grid, verbose=V) 
    lastChoice = -1
    if r == 1:
        print("Congrats player 1!")
        return 1
    if r == 2:
        print("Congrats player 2!")
        return 2
    if r == 3:
        print("Tie. Good game.")
        return 3
    if r == 0 or r == -1:
        print("Eror upstream.")
        return -1
    else:
        print("Error.")
        return None

if __name__ == '__main__':
    while True:
        s = raw_input('Select mode:\n player v player (1),\n player v computer (2),\n computer v player (3),\n or computer v computer (4):\n\n')
        if s == '1' or s == '(1)':
            game(1)
            break
        elif s == '2' or s == '(2)':
            game(2)
            break
        elif s == '3' or s == '(3)':
            game(3)
            break
        elif s == '4' or s == '(4)':
            game(4)
            break
        else:
            print("Undefined input\n\n")



