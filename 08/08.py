from icecream import ic

with open("08.input", "r") as f:
    data = list(x.strip().split(' | ') for x in f)

Answer1 = 0
for signals, digits in data:
    for digit in digits.split():
        if len(digit) in [2, 3, 4, 7]:
            Answer1 += 1
ic(Answer1)

# 2 segments = 1 [cf]
# 3 segments = 7 [acf]
# 4 segments = 4 [bcdf]
# 5 segments = 2 [acdeg], 3 [acdfg], 5 [abdfg]
# 6 segments = 0 [abcefg], 6 [abdefg], 9 [abcdfg]
# 7 segments = 8 [abcdefg]
encoding = {str(i): None for i in range(10)}
for signals, digits in data:
    for signal in signals:
        if len(signal) == 2:
            encoding["1"] = signal
        elif len(signal) == 3:
            encoding["7"] = signal
        elif len(signal) == 4:
            encoding["4"] = signal
        elif len(signal) == 7:
            encoding["8"] = signal
        # 2, 3, 5 share 3 common segments
        # 3 = 1 + the 3 commons segments
        # 5 = common segments
