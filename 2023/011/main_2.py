from itertools import combinations

with open("input.txt", "r") as f:
    data = [
        [int(x.replace("#", "1").replace(".", "0")) for x in line.strip()]
        for line in f.readlines()
    ]

rows = [sum(data[line]) == 0 for line in range(len(data))]
cols = [
    sum([data[row][column] for row in range(len(data))]) == 0
    for column in range(len(data[0]))
]

new_data = []
shift = 0
index = 1
pos = {}

mult = 1000000
for row in range(len(data)):
    for col in range(len(data[0])):
        if data[row][col] == 1:
            pos[index] = (
                row + sum(rows[:row]) * (mult - 1),
                col + sum(cols[:col]) * (mult - 1),
            )
            index += 1

total = 0
for items in list(combinations(pos.values(), 2)):
    dist = abs(items[0][0] - items[1][0]) + abs(items[0][1] - items[1][1])
    total += dist

print(total)
