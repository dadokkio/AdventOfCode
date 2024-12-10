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

nodes = {
    f"{pos[i]['x'] + (pos[j]['x'] - pos[i]['x']) * 2},{pos[i]['y'] + (pos[j]['y'] - pos[i]['y']) * 2}"
    for pos in antennas.values()
    for i, j in itertools.product(range(len(pos)), repeat=2)
    if i != j
    and 0 <= pos[i]["x"] + (pos[j]["x"] - pos[i]["x"]) * 2 < width
    and 0 <= pos[i]["y"] + (pos[j]["y"] - pos[i]["y"]) * 2 < height
}

print(len(nodes))
