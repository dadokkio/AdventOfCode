from functools import lru_cache

with open("input.txt") as f:
    stones = [int(x) for x in f.read().split()]


@lru_cache(maxsize=None)
def blink(stone):
    if stone == 0:
        return 1
    stone_len = len(f"{stone}")
    if stone_len % 2 == 0:
        left = stone // 10 ** (stone_len // 2)
        right = stone - left * 10 ** (stone_len // 2)
        return left, right
    return stone * 2024


def flatten(items):
    ret = []
    for item in items:
        if isinstance(item, (list, tuple)):
            ret.extend(iter(item))
        else:
            ret.append(item)
    return ret


for _ in range(25):
    stones = flatten([blink(x) for x in stones])
print(len(stones))
