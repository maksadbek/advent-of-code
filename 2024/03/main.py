import re

pattern = re.compile("mul\\((\\d+),(\\d+)\\)")

with open("./input.txt") as file:
    acc = 0

    for line in file:
        for a, b in pattern.findall(line):
            acc += int(a) * int(b)

    print(acc)