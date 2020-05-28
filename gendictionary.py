from util import *

## Runs once; creates the global dictionaries for use.

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


