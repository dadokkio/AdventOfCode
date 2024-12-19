from pathlib import Path


DIR_MAP = {
    "^": 1j,
    ">": 1,
    "v": -1j,
    "<": -1,
}


def parse_grid(raw):
    start = 0
    grid = {}
    for i, row in enumerate(raw.split("\n")):
        for r, char in enumerate(row):
            grid[complex(r, -i)] = char
            if char == "@":
                start = complex(r, -i)
                grid[start] = "."
    return start, grid


def move(robot):
    for move in moves:
        if grid[robot + move] == ".":
            robot += move
        elif grid[robot + move] == "#":
            continue
        else:
            nb = 1
            while grid[robot + nb * move] not in ".#":
                nb += 1
            if grid[robot + nb * move] == "#":
                continue
            grid[robot + nb * move] = "O"
            grid[robot + move] = "."
            robot += move


if __name__ == "__main__":
    with Path("input.txt").open("r") as f:
        g, m = f.read().split("\n\n")
    robot, grid = parse_grid(g)
    moves = [DIR_MAP[direction] for direction in m if direction != "\n"]
    move(robot)
    print(
        sum(
            int(-100 * pos.imag + pos.real) for pos, item in grid.items() if item == "O"
        )
    )
