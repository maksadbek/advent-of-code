with open("./input.txt") as file:
    XMAS = "XMAS"
    matrix = [line for line in file]

    def search(a, b, step, direction):
        if step == len(XMAS):
            return 1

        acc = 0
        if 0 <= a+direction[0] < len(matrix) and 0 <= b+direction[1] < len(matrix[0]):
            if matrix[a+direction[0]][b+direction[1]] == XMAS[step]:
                acc += search(a+direction[0], b+direction[1], step+1, direction)

        return acc

    DIRECTIONS = (
        (+0, +1),
        (+0, -1),
        (-1, +0),
        (+1, +0),
        (+1, +1),
        (+1, -1),
        (-1, -1),
        (-1, +1),
    )

    ans = 0

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == XMAS[0]:
                for d in DIRECTIONS:
                    ans += search(i, j, 1, d)

    print(ans)