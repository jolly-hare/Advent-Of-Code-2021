from icecream import ic
from collections import defaultdict


def fuel_cost1(data):
    costs = defaultdict(int)
    for target in range(max(data)):
        for crab in data:
            costs[target] += abs(crab-target)
    return min(costs.values())


def fuel_cost2(data):
    costs = defaultdict(int)
    for target in range(max(data)):
        for crab in data:
            costs[target] += int(abs(crab-target)*((abs(crab-target)+1)/2))
    return min(costs.values())


crabs = [int(a) for a in open("07.input", "r").read().split(',')]
test_data = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]
assert fuel_cost1(test_data) == 37
assert fuel_cost1(crabs) == 325528
ic(fuel_cost1(crabs))

assert fuel_cost2(test_data) == 168
assert fuel_cost2((crabs)) == 85015836
ic(fuel_cost2(crabs))
