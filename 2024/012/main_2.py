from collections import deque

DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def get_turn_contribution(point, adjacent_nodes, nodes, single):
    (row_a, col_a), (row_b, col_b) = adjacent_nodes

    if row_a == row_b or col_a == col_b:
        return 0

    if single:
        return (
            1
            if (row_a == point[0] and (row_b, col_a) in nodes)
            or (row_b == point[0] and (row_a, col_b) in nodes)
            else 2
        )
    return (
        1
        if (row_a == point[0] and (row_b, col_a) not in nodes)
        or (row_b == point[0] and (row_a, col_b) not in nodes)
        else 0
    )


def get_perimeter(nodes):
    perimeter = 0
    for row, col in nodes:
        adj_nodes = [
            (row + step_row, col + step_col)
            for step_row, step_col in DIRECTIONS
            if (row + step_row, col + step_col) in nodes
        ]

        if not adj_nodes:
            perimeter += 4
        elif len(adj_nodes) == 1:
            perimeter += 2
        elif len(adj_nodes) == 2:
            perimeter += get_turn_contribution((row, col), adj_nodes, nodes, True)
        else:
            perimeter += sum(
                get_turn_contribution(
                    (row, col), [adj_nodes[i], adj_nodes[j]], nodes, False
                )
                for i in range(len(adj_nodes) - 1)
                for j in range(i + 1, len(adj_nodes))
            )
    return perimeter


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
