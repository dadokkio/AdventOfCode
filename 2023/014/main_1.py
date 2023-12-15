import numpy as np


def count_zero(array):
    nrows, ncols = array.shape
    return sum(np.count_nonzero(array[j] == "O") * (ncols - j) for j in range(nrows))


def tilt(array):
    nrows, ncols = array.shape
    for j in range(ncols):
        empty_row = []
        for i in range(nrows):
            if array[i, j] == "O":
                if len(empty_row) != 0:
                    space = empty_row.pop(0)
                    array[space[0], j] = "O"
                    array[i, j] = "."
                    empty_row.append([i, j])
            elif array[i, j] == ".":
                empty_row.append([i, j])
            elif array[i, j] == "#":
                empty_row = []
    return array


with open("input.txt") as file:
    data = np.array([list(line.strip()) for line in file.readlines()])
    print(count_zero(tilt(data)))
