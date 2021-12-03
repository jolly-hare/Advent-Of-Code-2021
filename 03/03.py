from icecream import ic

with open("03.input", "r") as f:
    lines = [x.strip() for x in f]

bit_sums = [0]*len(lines[0])
gamma_bits = ''
epsilon_bits = ''
for line in lines:
    line_ints = zip(bit_sums, [int(a) for a in list(line)])
    bit_sums = [x + y for (x, y) in line_ints]
for idx, digit in enumerate(bit_sums):
    if digit >= len(lines) / 2:
        gamma_bits += '1'
        epsilon_bits += '0'
    else:
        gamma_bits += '0'
        epsilon_bits += '1'
ic(int(gamma_bits, 2) * int(epsilon_bits, 2))  # Part 1 answer

oxygen_list = lines
cosrub_list = lines
for i in range(len(lines[0])):
    if len(oxygen_list) > 1:
        oxy_zeros = [x for x in oxygen_list if x[i] == '0']
        oxy_ones = [x for x in oxygen_list if x[i] == '1']
        if len(oxy_ones) >= len(oxy_zeros):
            oxygen_list = oxy_ones
        else:
            oxygen_list = oxy_zeros

    if len(cosrub_list) > 1:
        co_zeros = [x for x in cosrub_list if x[i] == '0']
        co_ones = [x for x in cosrub_list if x[i] == '1']
        if len(co_ones) >= len(co_zeros):
            cosrub_list = co_zeros
        else:
            cosrub_list = co_ones
ic(int(oxygen_list[0], 2) * int(cosrub_list[0], 2))  # Part 2 Answer
