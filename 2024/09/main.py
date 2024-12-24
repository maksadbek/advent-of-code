with open("input.txt") as file:
    for line in file:
        file = list(map(int, list(line.strip())))
        file.append(0)  # add empty space count to the last file

        pairs = list(zip(file[::2], file[1::2]))

        l, r = 0, len(pairs) - 1

        nums = []

        while l <= r:
            a, b = pairs[l]
            nums += a * [str(l)]

            while b and l < r:
                cap = min(b, pairs[r][0])
                nums += [str(r)] * cap

                pairs[r] = (pairs[r][0] - cap, pairs[r][1])

                b -= cap
                if not b:
                    break

                r -= 1

            l += 1

        print(sum([i * x for i, x in enumerate(map(int, nums))]))
