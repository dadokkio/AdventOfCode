import itertools
from pprint import pprint

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
for row in range(len(data)):
    new_data.append([])
    for col in range(len(data[0])):
        if cols[col]:
            new_data[row + shift].append(0)
            new_data[row + shift].append(0)
        else:
            if data[row][col] == 1:
                new_data[row + shift].append(index)
                pos[index] = (row + shift, len(new_data[row + shift]) - 1)
                index += 1
            else:
                new_data[row + shift].append(0)
    if rows[row]:
        new_data.append([0] * (len(data[0]) + sum(cols)))
        shift += 1

total = 0
for items in list(itertools.combinations(pos.values(), 2)):
    dist = abs(items[0][0] - items[1][0]) + abs(items[0][1] - items[1][1])
    total += dist

pprint(new_data)
print(total)
