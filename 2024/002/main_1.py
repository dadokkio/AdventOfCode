ret = 0
with open("input.txt", "r") as file:
    for line in file:
        nums = list(map(int, line.split()))
        if all(x > y and x <= y + 3 for x, y in zip(nums, nums[1:])) or all(
            x < y and x + 3 >= y for x, y in zip(nums, nums[1:])
        ):
            ret += 1

print(ret)
