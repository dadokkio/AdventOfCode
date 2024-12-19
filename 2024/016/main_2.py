from queue import PriorityQueue
from collections import defaultdict

DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def find_start_end_positions(lines):
    return next(
        (r, c)
        for r in range(len(lines))
        for c in range(len(lines[r]))
        if lines[r][c] == "S"
    ), next(
        (r, c)
        for r in range(len(lines))
        for c in range(len(lines[r]))
        if lines[r][c] == "E"
    )


def is_valid_move(lines, r_n, c_n, current_direction, next_direction):
    return (
        0 <= r_n < len(lines)
        and 0 <= c_n < len(lines[0])
        and lines[r_n][c_n] != "#"
        and next_direction[0] * current_direction[0]
        + next_direction[1] * current_direction[1]
        >= 0
    )


def main(lines, start_position, end_position):
    init_direction = (0, 1)
    g_score = {(start_position, init_direction): 0}
    points_path_map = defaultdict(list)

    queue = PriorityQueue()
    queue.put(item=(0, start_position, init_direction, [start_position]))

    while not queue.empty():
        points, current_position, current_direction, path = queue.get()
        if current_position == end_position:
            points_path_map[points].append(path)

        r, c = current_position
        for next_direction in DIRECTIONS:
            step_r, step_c = next_direction
            r_n, c_n = (r + step_r), (c + step_c)

            if not is_valid_move(lines, r_n, c_n, current_direction, next_direction):
                continue

            cost = 1 if current_direction == next_direction else 1001
            tentative_g_score = g_score[(current_position, current_direction)] + cost

            state_key = ((r_n, c_n), next_direction)
            g_score.setdefault(state_key, float("inf"))

            if tentative_g_score <= g_score[state_key]:
                g_score[state_key] = tentative_g_score
                queue.put(
                    item=(
                        points + cost,
                        (r_n, c_n),
                        next_direction,
                        path + [(r_n, c_n)],
                    )
                )

    min_score = min(points_path_map.keys())
    return len({tile for path in points_path_map[min_score] for tile in path})


if __name__ == "__main__":
    with open(file="input.txt", mode="r") as f:
        lines = [line.strip() for line in f.readlines()]
    start_position, end_position = find_start_end_positions(lines)
    print(main(lines, start_position, end_position))
