import os
from multiprocessing import Pool

DEBUG = False


def start(data):
    for idr, row in enumerate(data):
        if "^" in row:
            idc = row.index("^")
            data[idr][idc] = "S"
            break
    return idr, idc


def up(data, idr, idc):
    while idr > 0 and data[idr - 1][idc] not in ["#", "O"]:
        idr -= 1
        if data[idr][idc] == ".":
            data[idr][idc] = "^"
    return idr, idc


def right(data, idr, idc):
    while idc < len(data[0]) - 1 and data[idr][idc + 1] not in ["#", "O"]:
        idc += 1
        if data[idr][idc] == ".":
            data[idr][idc] = ">"
    return idr, idc


def left(data, idr, idc):
    while idc > 0 and data[idr][idc - 1] not in ["#", "O"]:
        idc -= 1
        if data[idr][idc] == ".":
            data[idr][idc] = "<"
    return idr, idc


def down(data, idr, idc):
    while idr < len(data) - 1 and data[idr + 1][idc] not in ["#", "O"]:
        idr += 1
        if data[idr][idc] == ".":
            data[idr][idc] = "v"
    return idr, idc


def out(data, idr, idc):
    if idr <= 0 or idr >= len(data) - 1:
        return True
    return idc <= 0 or idc >= len(data[0]) - 1


def out_print(data, id_row, id_cell):
    with open(
        f"out/out_{id_row}_{id_cell}.txt",
        "w",
    ) as f:
        for row in data:
            f.write("".join(row))
            f.write("\n")


def main(data):
    original_data, original_idr, original_idc, id_row, id_cell = data
    data = [row[:] for row in original_data]
    idr, idc = original_idr, original_idc

    data[id_row][id_cell] = "O"
    all_steps = []
    idf = 0

    while True:
        idr, idc = functions[idf](data, idr, idc)
        if out(data, idr, idc):
            return False
        if (idr, idc, idf) in all_steps:
            if DEBUG:
                out_print(data, id_row, id_cell)
            return True
        all_steps.append((idr, idc, idf))
        idf = (idf + 1) % 4


if __name__ == "__main__":
    functions = [up, right, down, left]
    loops = 0

    with open("input.txt", "r") as f:
        original_data = [list(line.strip()) for line in f]
    original_idr, original_idc = start(original_data)

    cpu_count = os.cpu_count()
    with Pool(cpu_count) as p:
        results = p.map(
            main,
            [
                (original_data, original_idr, original_idc, id_row, id_cell)
                for id_row, row in enumerate(original_data)
                for id_cell, cell in enumerate(row)
                if cell not in ["#", "^"]
            ],
        )

    print(sum(results))
