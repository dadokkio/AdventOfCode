data = [list(y) for y in open("input.txt", "r").readlines()]

DEBUG = False


def start():
    for idr, row in enumerate(data):
        if "^" in row:
            idc = row.index("^")
            data[idr][idc] = "S"
            break
    if DEBUG:
        print("🚀", "r:", f"{idr:03}", "c:", f"{idc:03}", "size: 000")
    return idr, idc


def up(idr, idc):
    size = 0
    while idr > 0 and data[idr - 1][idc] != "#":
        idr -= 1
        if data[idr][idc] == ".":
            data[idr][idc] = "^"
            size += 1
    if DEBUG:
        print("⬆️", "r:", f"{idr:03}", "c:", f"{idc:03}", "size:", f"{size:03}")
    return idr, idc, size


def right(idr, idc):
    size = 0
    while idc < len(data[0]) - 1 and data[idr][idc + 1] != "#":
        idc += 1
        if data[idr][idc] == ".":
            data[idr][idc] = ">"
            size += 1
    if DEBUG:
        print("➡️", "r:", f"{idr:03}", "c:", f"{idc:03}", "size:", f"{size:03}")
    return idr, idc, size


def left(idr, idc):
    size = 0
    while idc > 0 and data[idr][idc - 1] != "#":
        idc -= 1
        if data[idr][idc] == ".":
            data[idr][idc] = "<"
            size += 1
    if DEBUG:
        print("⬅️", "r:", f"{idr:03}", "c:", f"{idc:03}", "size:", f"{size:03}")
    return idr, idc, size


def down(idr, idc):
    size = 0
    while idr < len(data) - 1 and data[idr + 1][idc] != "#":
        idr += 1
        if data[idr][idc] == ".":
            data[idr][idc] = "v"
            size += 1
    if DEBUG:
        print("⬇️", "r:", f"{idr:03}", "c:", f"{idc:03}", "size:", f"{size:03}")
    return idr, idc, size


def out(idr, idc):
    if idr <= 0 or idr >= len(data) - 1:
        return True
    return idc <= 0 or idc >= len(data[0]) - 1


if __name__ == "__main__":
    functions = [up, right, down, left]
    steps = idf = 0
    idr, idc = start()
    while True:
        idr, idc, size = functions[idf](idr, idc)
        if out(idr, idc):
            break
        idf = (idf + 1) % 4
        steps += size
    print("TOT:", steps - 1)

    if DEBUG:
        with open("out__1.txt", "w") as f:
            for row in data:
                f.write("".join(row))
