import numpy as np


def area(x, y):
    return 0.5 * np.abs(np.dot(x, np.roll(y, 1)) - np.dot(y, np.roll(x, 1)))


loc = (0, 0)
xs = []
ys = []
directions = [(0, 1), (-1, 0), (0, -1), (1, 0)]
num_pts = 0
for line in open("input.txt", "r"):
    a, b, c = line.split()

    cur_dir = directions[int(c[-2])]
    cur_len = int(c[2:-2], 16)

    num_pts += cur_len
    loc = (loc[0] + cur_len * cur_dir[0], loc[1] + cur_len * cur_dir[1])
    xs.append(loc[0])
    ys.append(loc[1])

I = area(xs, ys) + 1 - num_pts // 2
print(int(I + num_pts))
