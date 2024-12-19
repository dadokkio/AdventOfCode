import itertools

GRID_SIZE = 70
DIRECTIONS = [1, -1, 1j, -1j]
START = 0
GOAL = complex(GRID_SIZE, GRID_SIZE)


def main():
    with open("input.txt") as f:
        coordinates = [
            complex(x, y) for line in f for x, y in [map(int, line.strip().split(","))]
        ]
    walls = set(coordinates[:1024])

    front, seen = {START}, {START}
    steps = 0

    while front:
        steps += 1
        new_positions = set()

        for current_pos, direction in itertools.product(front, DIRECTIONS):
            next_pos = current_pos + direction

            if next_pos == GOAL:
                return steps

            if (
                0 <= next_pos.real <= GRID_SIZE
                and 0 <= next_pos.imag <= GRID_SIZE
                and next_pos not in walls
                and next_pos not in seen
            ):
                seen.add(next_pos)
                new_positions.add(next_pos)

        front = new_positions

    return 0


print(main())
