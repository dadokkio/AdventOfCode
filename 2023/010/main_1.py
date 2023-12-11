directions = {
    "su": (-1, 0),
    "gi": (1, 0),
    "sx": (0, -1),
    "dx": (0, 1),
}


def is_valid(label, previous, value):
    if value in ["|", "F", "7"] and label == "su" and previous in ["|", "J", "L", "S"]:
        return True
    elif (
        value in ["|", "L", "J"] and label == "gi" and previous in ["|", "F", "7", "S"]
    ):
        return True
    elif (
        value in ["-", "L", "F"] and label == "sx" and previous in ["-", "J", "7", "S"]
    ):
        return True
    elif (
        value in ["-", "J", "7"] and label == "dx" and previous in ["-", "F", "L", "S"]
    ):
        return True
    elif value == "S" and label == "su" and previous in ["|", "J", "L"]:
        return True
    elif value == "S" and label == "gi" and previous in ["|", "7", "F"]:
        return True
    elif value == "S" and label == "sx" and previous in ["-", "7", "J"]:
        return True
    elif value == "S" and label == "dx" and previous in ["-", "L", "F"]:
        return True
    return False


moves = []

with open("input.txt", "r") as f:
    data = f.readlines()
    for line in range(len(data)):
        if data[line].find("S") != -1:
            start = (line, data[line].find("S"))
            print(f"Start: {start[0]+1}, {start[1]+1}")

    last = start
    previous = None
    ok = False

    while True:
        for label, dir in directions.items():
            new = (last[0] + dir[0], last[1] + dir[1])

            if (
                new[0] < 0
                or new[0] > len(data) - 1
                or new[1] > len(data[0]) - 2
                or new[1] < 0
            ):
                # print(f"Out of bounds {new[0]+1}, {new[1]+1}")
                continue
            if new == previous:
                # print(f"Going back {new[0]+1}, {new[1]+1}")
                continue
            if is_valid(label, data[last[0]][last[1]], data[new[0]][new[1]]):
                previous = last
                moves.append(new)
                print(
                    f"Moving {label} to {new[0]+1}, {new[1]+1}: {data[last[0]][last[1]]}{data[new[0]][new[1]]}"
                )
                last = new

                if data[new[0]][new[1]] == "S":
                    ok = True
                    print(f"END {new[0]+1}, {new[1]+1}")
                    break
        if ok:
            break

    print(f"Moves: {len(moves)}")
