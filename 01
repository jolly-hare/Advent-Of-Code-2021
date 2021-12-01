from icecream import ic

# PART 1
# count increases
part1example_data = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
part1example_answer = 7
myfile = open("input01", "r")
data = [int(a) for a in myfile.read().split()]
#data = part1example_data
increases1 = 0
for i, j in enumerate(data):
    if j > data[i-1]:
        increases1 += 1
if increases1 == part1example_answer:
    ic("example 1 passes")
else:
    ic(increases1)

# PART 2
# sliding window sum of threes, then count increases
# same data
part2example_answer = 5
increases2 = 0
old_window = 0
for i, j in enumerate(data):
    window = sum(data[i-2:i+1])
    if window > old_window and old_window != 0:
        increases2 += 1
    old_window = window
if increases2 == part2example_answer:
    ic("example 2 passes: ", increases2)
else:
    ic(increases2)
