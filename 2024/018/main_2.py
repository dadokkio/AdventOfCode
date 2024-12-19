WIDTH, HEIGHT = 70, 70


def bfs(walls):
    start, goal = (0, 0), (WIDTH, HEIGHT)
    queue, seen = [(start, 0)], {start}
    while queue:
        (x, y), steps = queue.pop(0)
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = x + dx, y + dy
            if (nx, ny) == goal:
                return steps + 1
            if (
                0 <= nx <= WIDTH
                and 0 <= ny <= HEIGHT
                and (nx, ny) not in walls
                and (nx, ny) not in seen
            ):
                seen.add((nx, ny))
                queue.append(((nx, ny), steps + 1))
    return 0


def find_first(coordinates):
    low, high = 0, len(coordinates)
    while high - low > 1:
        mid = (low + high) // 2
        if bfs(set(coordinates[:mid])):
            low = mid
        else:
            high = mid
    return coordinates[low]


if __name__ == "__main__":
    with open("input.txt") as f:
        coordinates = [tuple(map(int, line.strip().split(","))) for line in f]
    first_x, first_y = find_first(coordinates)
    print(f"{first_x},{first_y}")
