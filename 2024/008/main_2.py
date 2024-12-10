import itertools

with open("input.txt", "r") as f:
    grid = f.read().strip().split("\n")

width, height = len(grid[0]), len(grid)
antennas = {
    frequency: [
        {"x": x, "y": y}
        for y, x in itertools.product(range(height), range(width))
        if grid[y][x] == frequency
    ]
    for frequency in set("".join(grid))
    if frequency != "."
}

nodes = set()
for pos in antennas.values():
    for i, j in itertools.combinations(range(len(pos)), 2):
        dx = pos[j]["x"] - pos[i]["x"]
        dy = pos[j]["y"] - pos[i]["y"]

        for k in range(-50, 50):
            x = pos[i]["x"] + dx * k
            y = pos[i]["y"] + dy * k

            if 0 <= x < width and 0 <= y < height:
                nodes.add(f"{x},{y}")

print(len(nodes))
