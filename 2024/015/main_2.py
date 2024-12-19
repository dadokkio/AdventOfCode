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
            if char in ".#":
                grid[complex(2 * r, -i)] = char
                grid[complex(2 * r + 1, -i)] = char
            elif char == "O":
                grid[complex(2 * r, -i)] = "["
                grid[complex(2 * r + 1, -i)] = "]"
            else:
                grid[complex(2 * r, -i)] = "."
                grid[complex(2 * r + 1, -i)] = "."
                start = complex(2 * r, -i)
    return start, grid


def can_move_vertically(pos, direction):
    if grid[pos] not in ["]", "["]:
        return grid[pos] == "."
    delta = -1 if grid[pos] == "]" else 1
    if grid[pos + direction] == "." and grid[pos + direction + delta] == ".":
        return True
    if grid[pos + direction] == "#" or grid[pos + direction + delta] == "#":
        return False
    return can_move_vertically(pos + direction, direction) and can_move_vertically(
        pos + direction + delta, direction
    )


def move_vertically(pos, direction):
    if grid[pos] == "]":
        delta = -1
    elif grid[pos] == "[":
        delta = 1
    else:
        return None
    while grid[pos + direction] != "." or grid[pos + direction + delta] != ".":
        move_vertically(pos + direction, direction)
        move_vertically(pos + direction + delta, direction)
    grid[pos + direction] = grid[pos]
    grid[pos + direction + delta] = grid[pos + delta]
    grid[pos] = "."
    grid[pos + delta] = "."


def can_move_horizontally(pos, direction):
    while True:
        char = grid[pos + 2 * direction]
        if char == "#":
            return False
        if char == ".":
            return True
        pos += 2 * direction


def move_horizontally(pos, direction):
    while grid[pos + 2 * direction] != ".":
        move_horizontally(pos + 2 * direction, direction)
    grid[pos + 2 * direction] = grid[pos + direction]
    grid[pos + direction] = grid[pos]
    grid[pos] = "."


def robot_move(robot):
    for move in moves:
        next_pos = robot + move

        if grid[next_pos] == ".":
            robot = next_pos
            continue

        if grid[next_pos] == "#":
            continue

        if move in (1, -1) and can_move_horizontally(next_pos, move):
            move_horizontally(next_pos, move)
            robot += move
        elif move not in (1, -1) and can_move_vertically(next_pos, move):
            move_vertically(next_pos, move)
            robot += move

    return robot


if __name__ == "__main__":
    with Path("input.txt").open("r") as f:
        g, m = f.read().split("\n\n")
    robot, grid = parse_grid(g)
    moves = [DIR_MAP[direction] for direction in m if direction != "\n"]
    robot_move(robot)
    print(
        sum(
            int(-100 * pos.imag + pos.real) for pos, item in grid.items() if item == "["
        )
    )
