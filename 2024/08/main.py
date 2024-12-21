from collections import defaultdict

with open("./input.txt") as file:
    matrix = []
    positions = defaultdict(list)
    positions_idx = set()

    for row, line in enumerate(file):
        matrix.append(list(line.strip()))

        for col, ch in enumerate(line.strip()):
            if ch != ".":
                positions[ch].append((row, col))
                positions_idx.add((row, col))

    antinodes = set()

    for ch, p in positions.items():
        for i in range(len(p)):
            for j in range(i+1, len(p)):
                a = abs(p[i][0] - p[j][0])
                b = abs(p[i][1] - p[j][1])

                dx = (p[i][0] - p[j][0])
                dy = (p[i][1] - p[j][1])

                if (p[i][0]+dx, p[i][1]+dy) != p[j] and 0 <= p[i][0]+dx < len(matrix) and 0 <= p[i][1]+dy < len(matrix[0]):
                    m, n = p[i][0]+dx, p[i][1]+dy
                    while 0 <= m < len(matrix) and 0 <= n < len(matrix[0]):
                        if (m, n) not in positions_idx:
                            antinodes.add((m, n))

                        m += dx
                        n += dy

                if (p[i][0]-dx, p[i][1]-dy) != p[j] and 0 <= p[i][0]-dx < len(matrix) and 0 <= p[i][1]-dy < len(matrix[0]):
                    m, n = p[i][0]-dx, p[i][1]-dy

                    while 0 <= m < len(matrix) and 0 <= n < len(matrix[0]):
                        if (m, n) not in positions_idx:
                            antinodes.add((m, n))

                        m -= dx
                        n -= dy

                if (p[j][0]+dx, p[j][1]+dy) != p[i] and 0 <= p[j][0]+dx < len(matrix) and 0 <= p[j][1]+dy < len(matrix[0]):
                    m, n = p[j][0]+dx, p[j][1]+dy

                    while 0 <= m < len(matrix) and 0 <= n < len(matrix[0]):
                        if (m, n) not in positions_idx:
                            antinodes.add((m, n))

                        m += dx
                        n += dy

                if (p[j][0]-dx, p[j][1]-dy) != p[i] and 0 <= p[j][0]-dx < len(matrix) and 0 <= p[j][1]-dy < len(matrix[0]):
                    m, n = p[j][0]-dx, p[j][1]-dy

                    while 0 <= m < len(matrix) and 0 <= n < len(matrix[0]):
                        if (m, n) not in positions_idx:
                            antinodes.add((m, n))

                        m -= dx
                        n -= dy

    print(len(antinodes) + sum([len(positions[x]) for x in positions if len(positions[x]) > 1]))
