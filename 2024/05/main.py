from collections import defaultdict

with open("./input.txt") as file:
    order = defaultdict(list)

    for line in file:
        if line.isspace():
            break

        a, b = line.split("|")
        order[int(a)].append(int(b))

    acc = 0

    for line in file:
        m = set()

        nums = list(map(int, line.split(",")))
        done = False

        for n in nums:
            for o in order.get(n, []):
                if o in m:
                    done = True
                    break

            if done:
                break

            m.add(n)

        if not done:
            acc += nums[(len(nums) // 2)]

    print(acc)