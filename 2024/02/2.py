with open("./input.txt") as file:
    levels = [tuple(map(int, line.split())) for line in file]

    def is_safe(level):
        if level[0] == level[1]:
            return False

        deltas = (
            [level[i] - level[i - 1] for i in range(1, len(level))]
            if level[0] < level[1]
            else [level[i] - level[i + 1] for i in range(len(level) - 1)]
        )

        return all(0 < d <= 3 for d in deltas)

    print(sum(1 for level in levels if is_safe(level)))
