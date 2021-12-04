from icecream import ic
import numpy as np

f = open("04.input", "r").read()
drawn_nums = [int(a) for a in f.splitlines()[0].split(',')]
grids = []
drawn = []
size = 5
winning_grids = first_winning_number = first_winning_grid = first_winning_mask = []
last_winning_number = last_winning_grid = last_winning_mask = []

for lines in f.split('\n\n')[1:]:
    grid = []
    for line in lines.strip().split('\n'):
        grid.append([int(x) for x in line.split()])
    grids.append(grid)

for i in range(len(grids)):
    x = np.zeros((5, 5), dtype=bool)
    drawn.append(x)
first_winner = False
for i in drawn_nums:
    for x, grid in enumerate(grids):
        if x in winning_grids:
            continue
        for y in range(5):
            for z in range(5):
                if grids[x][y][z] == i:
                    assert drawn[x][y][z] == False
                    drawn[x][y][z] = True
        for r in range(5):
            if np.all(drawn[x][r] == True) or np.all(drawn[x][:, r] == True):
                if not first_winner:
                    first_winner = True
                    first_winning_grid = grids[x].copy()
                    first_winning_mask = drawn[x].copy()
                    first_winning_number = i
                    winning_grids.append(x)
                else:
                    last_winning_grid = grids[x].copy()
                    last_winning_mask = drawn[x].copy()
                    last_winning_number = i
                    winning_grids.append(x)

unmarked_sum_first = 0
for a in range(5):
    for b in range(5):
        if not first_winning_mask[a][b]:
            unmarked_sum_first += first_winning_grid[a][b]
Answer_1 = unmarked_sum_first * first_winning_number
ic(Answer_1)

unmarked_sum_last = 0
for c in range(5):
    for d in range(5):
        if not last_winning_mask[c][d]:
            unmarked_sum_last += last_winning_grid[c][d]
Answer_2 = unmarked_sum_last * last_winning_number
ic(Answer_2)
