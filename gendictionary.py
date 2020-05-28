from util import *

# Helper functions for creating / working with the table (dictionary) of value assignments.

## Initial RL value

def RLoutcome(grid, player):
    """Book explicily says, draws, losses = 0, wins = 1, intermediate = 0.5 default"""
    r = result(grid)
    if r == player:
        return 1
    elif r == 0:
        return 0.5
    else:
        return 0


## Functions for working with ternary numbers / hashing for dictionaries.

def ternary9(n):
    """Gets the leading 9 ternary digits for an integer."""
    r = []
    for i in range(9):
        r.append(n%3)
        n = n/3
    r.reverse()
    return np.array(r)

def bt(grid):
    return np.dot(hasher, grid.reshape(9))

### Workhorse for accessing the dictionaries later
def lookup(d, grid):
    return d[bt(grid)]


## Runs once; creates the global dictionaries for use.

def gen_dicts(retgrids = False):
    N = 3**9
    
    grids = []
    
    for n in range(N):
        g = ternary9(n).reshape(3, 3)
        if isvalid(g):
            grids.append(g)    
    
    v1 = [RLoutcome(grid, 1) for grid in grids]
    v2 = [RLoutcome(grid, 2) for grid in grids]
    
    keys = [bt(grid) for grid in grids]
    
    d1 = dict(zip(keys, v1))
    d2 = dict(zip(keys, v2))

    if retgrids:
        return d1, d2, grids

    return d1, d2

