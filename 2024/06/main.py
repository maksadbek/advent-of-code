with open("./input.txt") as file:
    UP = (-1, 0)
    DOWN = (1, 0)
    RIGHT = (0, 1)
    LEFT = (0, -1)

    matrix = [line for line in file]
    seen = set()
    stack = []

    def traverse():
        while stack:
            a, b, direction = stack.pop()
            seen.add((a, b))

            if 0 <= a+direction[0] < len(matrix) and 0 <= b+direction[1] < len(matrix[0]):
                next_a, next_b = a+direction[0], b+direction[1]
                
                if matrix[next_a][next_b] == "#":
                    if direction == UP:
                        stack.append((a + RIGHT[0], b + RIGHT[1], RIGHT))
                    elif direction == RIGHT:
                        stack.append((a + DOWN[0], b + DOWN[1], DOWN))
                    elif direction == DOWN:
                        stack.append((a + LEFT[0], b + LEFT[1], LEFT))
                    if direction == LEFT:
                        stack.append((a + UP[0], b + UP[1], UP))
                else:
                    stack.append((next_a, next_b, direction))

    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == "^":
                stack.append((row, col, UP))
                break

    traverse()

    print(len(seen))