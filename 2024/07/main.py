with open("input.txt") as file:
    ans = 0

    for line in file:
        parts = line.split(":")
        eq = int(parts[0])
        ops = list(map(int, parts[1].strip().split()))

        def traverse(ans: int, nums: list[int], acc: int, i: int):
            if i == len(nums):
                if acc == ans:
                    return True

                return False

            return any(
                [
                    traverse(ans, nums, acc + nums[i], i + 1),
                    traverse(ans, nums, acc * nums[i], i + 1),
                ]
            )

        if traverse(eq, ops, 0, 0):
            ans += eq

    print(ans)
