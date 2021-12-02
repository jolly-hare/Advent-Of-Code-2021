from icecream import ic
example = ("forward 5", "down 5",  "forward 8", "up 3", "down 8", "forward 2")

sub_down = 0
sub_forward = 0
sub_aim = 0
with open("02.input", "r") as f:
    lines = f.read().splitlines()
    for line in lines:
        direction, distance = line.split(' ')
        if direction == "forward":
            sub_forward += int(distance)
            sub_down += int(distance) * sub_aim
        if direction == "up":
            sub_aim -= int(distance)
        if direction == "down":
            sub_aim += int(distance)
    #part1_answer = sub_down * sub_forward
    #ic(part1_answer)
    part2_answer = sub_down * sub_forward
    ic(part2_answer)
