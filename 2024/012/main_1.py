from collections import deque

DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def get_perimeter(nodes):
    return sum(
        4
        - sum(
            (row + step_row, col + step_col) in nodes
            for step_row, step_col in DIRECTIONS
        )
        for row, col in nodes
    )


def find_region(lines, search_plant):
    queue = deque([search_plant])
    visited = set()
    plant = lines[search_plant[0]][search_plant[1]]

    while queue:
        row, col = queue.pop()
        visited.add((row, col))

        for step_row, step_col in DIRECTIONS:
            new_row, new_col = row + step_row, col + step_col
            if (
                0 <= new_row < len(lines)
                and 0 <= new_col < len(lines[0])
                and lines[new_row][new_col] == plant
                and (new_row, new_col) not in visited
            ):
                queue.append((new_row, new_col))
    return visited


with open("input.txt", "r") as f:
    lines = [x.strip() for x in f.readlines()]

letter_pos = {(row, col) for row in range(len(lines)) for col in range(len(lines[row]))}
total_price = 0

while letter_pos:
    search_plant = letter_pos.pop()
    visited = find_region(lines, search_plant)
    area = len(visited)
    perimeter = get_perimeter(visited)
    total_price += area * perimeter
    letter_pos -= visited

print(total_price)
