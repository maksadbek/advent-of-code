with open("./input.txt") as file:
    pairs = [tuple(map(int, line.split())) for line in file]

    left, right = zip(*pairs)

    ans = sum(abs(a - b) for a, b in zip(sorted(left), sorted(right)))

    print(ans)