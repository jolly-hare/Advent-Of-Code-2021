from icecream import ic
from collections import defaultdict


def solve(data, days):
    counts = defaultdict(int)
    for i in data:
        counts[i] += 1
    for j in range(days):
        temp = defaultdict(int)
        for k, v in counts.items():
            if k == 0:
                temp[6] += v
                temp[8] += v
            else:
                temp[k-1] += v
        counts = temp
    return sum(counts.values())


fish_ages = [int(a) for a in open("06.input", "r").read().split(',')]
test_data = [3, 4, 3, 1, 2]
ic(solve(fish_ages, 80))
ic(solve(fish_ages, 256))
