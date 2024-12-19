from dataclasses import dataclass
from pathlib import Path
from itertools import groupby

WIDTH = 101
HEIGHT = 103


@dataclass
class Robot:
    x: int
    y: int
    vx: int
    vy: int


def move(robots, duration):
    for r in robots:
        r.x = (r.x + r.vx * duration) % WIDTH
        r.y = (r.y + r.vy * duration) % HEIGHT


def safety_factor(robots):
    quadrant = {"TL": 0, "TR": 0, "BL": 0, "BR": 0}
    for r in robots:
        if r.x < WIDTH // 2:
            if r.y < HEIGHT // 2:
                quadrant["BL"] += 1
            elif r.y > HEIGHT // 2:
                quadrant["TL"] += 1
        elif r.x > WIDTH // 2:
            if r.y < HEIGHT // 2:
                quadrant["BR"] += 1
            elif r.y > HEIGHT // 2:
                quadrant["TR"] += 1
    result = 1
    for nb in quadrant.values():
        result *= nb
    return result


def has_frame(robots):
    y_groups = {}
    for robot in robots:
        y_groups.setdefault(robot.y, []).append(robot.x)

    for x_coords in y_groups.values():
        if len(x_coords) < 25:
            continue

        x_coords.sort()
        consecutive = 1
        max_consecutive = 1

        for i in range(1, len(x_coords)):
            if x_coords[i] == x_coords[i - 1] + 1:
                consecutive += 1
                max_consecutive = max(max_consecutive, consecutive)
            else:
                consecutive = 1

        if max_consecutive > 25:
            return True

    return False


def find_tree(robots):
    duration = 0
    frame = has_frame(robots)
    while duration < 142000 and not frame:
        move(robots, 1)
        frame = has_frame(robots)
        duration += 1
    return duration


if __name__ == "__main__":
    robots = []
    with Path("input.txt").open("r") as f:
        robots = [
            Robot(*map(int, p[2:].split(",") + v[2:].split(",")))
            for line in f
            for p, v in [line.strip().split()]
        ]

    print(find_tree(robots))
