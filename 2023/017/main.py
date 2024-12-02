from heapq import heappush, heappop

with open("input.txt", "r") as file:
    data = file.read().splitlines()

sparse = {(i, j): int(c) for i, line in enumerate(data) for j, c in enumerate(line)}
n, m = len(data), len(data[0])
dirs = [(1, 0), (0, -1), (-1, 0), (0, 1)]


def solve(moves_min, moves_max):
    heap = [(0, (0, 0), (0, 0))]
    visited = {((0, 0), (0, 0))}
    while len(heap):
        cost, pos, lsdir = heappop(heap)
        for direction in range(-1, 2):
            if (direction == 0 and lsdir[1] == moves_max) or (
                direction != 0 and 0 < lsdir[1] < moves_min
            ):
                continue
            idx = lsdir[1] + 1 if direction == 0 and lsdir[1] != moves_max else 1
            ndi = (lsdir[0] + direction) % 4
            npos = tuple(sum(x) for x in zip(pos, dirs[ndi]))
            if npos in sparse and (npos, (ndi, idx)) not in visited:
                ncost = cost + sparse[npos]
                if npos == (n - 1, m - 1):
                    return ncost
                visited.add((npos, (ndi, idx)))
                heappush(heap, (ncost, npos, (ndi, idx)))


print(solve(0, 3))
print(solve(4, 10))
