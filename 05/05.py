from icecream import ic
from collections import defaultdict


def solve(lines, part):
    grid = defaultdict(int)
    for line in lines:
        x1, y1, x2, y2 = [int(a) for a in line.replace(' -> ', ',').split(',')]
        if x1 != x2 and y1 != y2:
            if part == '1':
                continue
        dx = (1 if x1 < x2 else (-1 if x1 > x2 else 0))
        dy = (1 if y1 < y2 else (-1 if y1 > y2 else 0))
        grid[(x1, y1)] += 1
        while x1 != x2 or y1 != y2:
            x1 += dx
            y1 += dy
            grid[(x1, y1)] += 1
    return grid


with open("05.input", "r") as f:
    data = list(x.strip() for x in f)

grid1 = solve(data, '1')
Answer1 = sum([1 for x in grid1.values() if x > 1])
ic(Answer1)

grid2 = solve(data, '2')
Answer2 = sum([1 for x in grid2.values() if x > 1])
ic(Answer2)
