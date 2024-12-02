with open("input.txt") as f:
    data = f.read().splitlines()
n = len(data)
sparse = {(i, j) for i in range(n) for j in range(n) if data[i][j] in ".S"}
S = next((i, j) for i in range(n) for j in range(n) if data[i][j] == "S")
dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

visited, new, cache = {S}, {S}, {0: 1}
k, r = divmod(26501365, n)

for c in range(1, r + 2 * n + 1):
    new_positions = set()
    for position in new:
        for direction in dirs:
            new_position = tuple(sum(x) for x in zip(position, direction))
            if (
                new_position not in visited
                and tuple(x % n for x in new_position) in sparse
            ):
                new_positions.add(new_position)
    visited, new = new, new_positions
    cache[c] = len(new) + (cache[c - 2] if c > 1 else 0)

d2 = cache[r + 2 * n] + cache[r] - 2 * cache[r + n]
d1 = cache[r + 2 * n] - cache[r + n]
print(cache[64])
print(cache[r + 2 * n] + (k - 2) * (2 * d1 + (k - 1) * d2) // 2)
