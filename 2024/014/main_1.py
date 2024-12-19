from dataclasses import dataclass
from pathlib import Path


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


if __name__ == "__main__":
    robots = []

    with Path("input.txt").open("r") as f:
        robots = [
            Robot(*map(int, p[2:].split(",") + v[2:].split(",")))
            for line in f
            for p, v in [line.strip().split()]
        ]

    move(robots, 100)
    print(safety_factor(robots))
