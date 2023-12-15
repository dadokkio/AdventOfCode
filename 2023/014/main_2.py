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


def spin(array):
    for _ in range(4):
        array = np.rot90(tilt(array), k=-1).copy()
    return array


with open("input.txt") as file:
    lines = [list(line.strip()) for line in file.readlines()]
    data = np.array(lines)
    all_data = []
    for end in range(200):
        data = spin(data)
        data_list = data.tolist()
        if data_list in all_data:
            start = all_data.index(data_list)
            break
        else:
            all_data.append(data_list)

    index = (999999999 - start) % (end - start) + start
    print(count_zero(np.array(all_data[index])))
