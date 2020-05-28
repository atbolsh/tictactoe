import numpy as np
import math
import os
from copy import deepcopy

# Main module full of helper functions with useful names. Main interface to numpy arrays.


## Main functions for calculating / making moves.
 
def availableMoves(grid):
    r = []
    for i in range(3):
        for j in range(3):
            if grid[i][j] == 0:
                r.append((i, j))
    return r

def move(grid, player, box):
    """Pass-by-valye, in order to explore opportunities downstream."""
    g2 = deepcopy(grid)
    g2[box[0]][box[1]] = player
    return g2

def moveIsValid(grid, box):
    return (grid[box[0]][box[1]] == 0)


## Helper functions for detecting gamestate (turn and completion)

def row_won(grid, rownum, player):
    return (grid[rownum][0] == player and 
           grid[rownum][1] == player and
           grid[rownum][2] == player)

def col_won(grid, colnum, player):
    return (grid[0][colnum] == player and 
           grid[1][colnum] == player and
           grid[2][colnum] == player)

def diag1_won(grid, player):
    return (grid[0][0] == player and
           grid[1][1] == player and
           grid[2][2] == player)

def diag2_won(grid, player):
    return (grid[0][2] == player and
           grid[1][1] == player and
           grid[2][0] == player)

def player_won(grid, player):
    if diag1_won(grid, player):
        return True
    if diag2_won(grid, player):
        return True
    for i in range(3):
        if row_won(grid, i, player):
            return True
        if col_won(grid, i, player):
            return True
    return False

def num_val(grid, val):
    num = 0
    for x in grid.reshape(9):
        if x == val:
            num += 1
    return num

def isfull(grid):
    return (num_val(grid, 0) == 0)



## Main functions detecting turn and completion.

def result(grid):
    """1 or 2 = that player won, 0 = not done, 3 = draw, -1 = error"""
    p1 = player_won(grid, 1)
    p2 = player_won(grid, 2)
    if p1 and p2:
        print("Grid impossible; both players won!")
        return -1
    if p1:
        return 1
    if p2:
        return 2
    if isfull(grid):
        return 3
    return 0

def turn(grid):
    """1 or 2 = that player; 0 = over; -1 = error."""
    r = result(grid)
    if r == -1:
        return -1 # error msg already printed
    num1 = num_val(grid, 1)
    num2 = num_val(grid, 2)
    if num2 == num1 - 1:
        if r == 0:
            return 2
        else:
            return 0
    elif num1 == num2:
        if r == 0:
            return 1
        else:
            return 0
    else:
        print("Grid impossible; double-check number of turns for players")
        return -1

def isvalid(grid):
    """Helper function to see if current grid could possibly be 
    an intermediate stage in a valid game. Wrapper around turn, 
    which already checks for both important pathologies 
    (too many from one player; both players won)."""
    if turn(grid) == -1:
        return False
    return True


## Functions for printing the current grid in a convenient way

def showRow(grid, r):
    print ' '.join([str(x) for x in list(grid[r])])
    return None

def showGrid(grid):
    print('\n\n')
    for i in range(3):
        showRow(grid, i)
    print('\n\n')
    return None

