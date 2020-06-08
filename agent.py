from util import *
from gendictionary import *


### This is the module with all the functions and objects relvant to learning resides.

### Have a "lastPicked" variable, by default set to -1. 
### Each time we get the opponents move back, we update ths score for lastPicked.

A = 0.5

pE = 0.3

# Dummy initial value.
#lastChoice = np.array([[0, 0, 0], [0, 1, 0], [0, 0, 0]])
lastChoice = -1

d1, d2 = gen_dicts()

def greedy_move(player, grid, valdict, alpha = A, verbose = False):
    if verbose:
        print("Greedy move chosen.\n\n")
    global lastChoice
    ## Lookahead, compute all possible positions after a move.
    freeSpots = availableMoves(grid)
    futures = [move(grid, player, box) for box in freeSpots]
    vals = np.array([lookup(valdict, f) for f in futures])
    if verbose:
        print("Possible futures and their values.\n\n")
        for i in range(len(vals)):
            print(vals[i])
            showGrid(futures[i])
            print("______________________\n")
    ## Now, select one of the the best choices and assign that to the output.
    M = max(vals)
    fullArray = [i for i in range(len(vals)) if vals[i] == M]
    ind = np.random.choice(fullArray)
    choice = futures[ind]
    if verbose:
        print("Chosen move:")
        showGrid(choice)
        print(vals[ind])
        print("______________________________\n\n")
    ## Update the valdict
    if type(lastChoice) != type(-1):
        if verbose:
            print("Updating valdict.\nlastChoice:\n")
            showGrid(lastChoice)
            print("Old value:   " + str(lookup(valdict, lastChoice)))
        valdict[bt(lastChoice)] += alpha*(lookup(valdict, choice) - lookup(valdict, lastChoice))
        if verbose:
            print("New value:   " + str(lookup(valdict, lastChoice)))
            print("_______________________\n\n")
    else:
        if verbose:
            print("No need to update valdict; lastChoice == -1.\n\n")
    ## Update lastchoice
    lastChoice = choice
    return choice

## Testing routine; it struggles with redefining global variables.

#grid = np.array([[0, 0, 0], [0, 1, 2], [0, 0, 0]])
#player = 1
#
#d1[bt(np.array([[0, 1, 0], [0, 1, 2], [0, 0, 0]]))] = 0.7
#d1[bt(np.array([[1, 0, 0], [0, 1, 2], [0, 0, 0]]))] = 0.7
#d1[bt(np.array([[0, 0, 1], [0, 1, 2], [0, 0, 0]]))] = 0.7
#
#choice = greedy_move(player, grid, d1, 0.2, verbose=True)
# 

def exploratory_move(player, grid, verbose=False):
    if verbose:
        print("Greedy move chosen.\n\n")
    global lastChoice
    ## Lookahead, compute all possible positions after a move and pick random one.
    freeSpots = availableMoves(grid)
    futures = [move(grid, player, box) for box in freeSpots]
    if verbose:
        print("Possible futures.\n\n")
        for i in range(len(futures)):
            showGrid(futures[i])
            print("______________________\n")
    ind = np.random.choice(np.arange(len(futures)))
    choice = futures[ind]
    if verbose:
        print("Chosen move:")
        showGrid(choice)
        print("______________________________\n\n")
    ## Update lastChoice and return
    lastChoice = choice
    return choice

def agent_move(player, grid, alpha=A, probExploration=pE, verbose=False):
    global d1
    global d2
    r = np.random.random()
    if r < probExploration:
        choice = exploratory_move(player, grid, verbose)
    else:
        if player == 1:
            valdict = d1
        else:
            valdict = d2
        choice = greedy_move(player, grid, valdict, alpha, verbose)
    return choice

def end_of_game(player, grid, alpha=A, verbose=False):
    global d1
    global d2
    if player == 1:
        valdict = d1
    else:
        valdict = d2

    if type(lastChoice) != type(-1):
        if verbose:
            print("Updating valdict.\nlastChoice:\n")
            showGrid(lastChoice)
            print("Old value:   " + str(lookup(valdict, lastChoice)))
        valdict[bt(lastChoice)] += alpha*(lookup(valdict, grid) - lookup(valdict, lastChoice))
        if verbose:
            print("New value:   " + str(lookup(valdict, lastChoice)))
            print("_______________________\n\n")
   
    return None



