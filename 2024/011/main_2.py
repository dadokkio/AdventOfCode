from collections import Counter

with open("input.txt") as file:
    stones = Counter(map(int, next(file).split()))

for _ in range(75):
    tmp_stones = Counter()
    for stone, n in stones.items():
        if stone == 0:
            tmp_stones[1] += n
        else:
            stone_len = len(str(stone))
            if stone_len % 2 == 0:
                half_len = stone_len // 2
                left = stone // 10**half_len
                right = stone % 10**half_len
                tmp_stones[left] += n
                tmp_stones[right] += n
            else:
                tmp_stones[2024 * stone] += n
    stones = tmp_stones

print(sum(stones.values()))
