import numpy as np


def area(x, y):
    return 0.5 * np.abs(np.dot(x, np.roll(y, 1)) - np.dot(y, np.roll(x, 1)))


loc = (0, 0)
xs = []
ys = []
directions = {
    "U": (1, 0),
    "D": (-1, 0),
    "L": (0, -1),
    "R": (0, 1),
}
pts = {(0, 0)}
for line in open("input.txt", "r"):
    a, b, c = line.split()
    cur_dir = directions[a]
    cur_len = int(b)
    for i in range(cur_len + 1):
        pts.add((loc[0] + i * cur_dir[0], loc[1] + i * cur_dir[1]))
    loc = (loc[0] + cur_len * cur_dir[0], loc[1] + cur_len * cur_dir[1])
    xs.append(loc[0])
    ys.append(loc[1])

print(int((area(xs, ys) + 1 - len(pts) // 2) + len(pts)))
