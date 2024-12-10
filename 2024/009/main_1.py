couples = []

with open("input.txt", "r") as f:
    data = f.read()
    for idx, x in enumerate(range(len(data) // 2)):
        couples.extend(idx for _ in range(int(data[x * 2])))
        couples.extend("." for _ in range(int(data[x * 2 + 1])))
    if len(data) % 2 != 0:
        couples.extend(idx + 1 for _ in range(int(data[-1])))

zipped = []
values = couples.copy()

for item in couples:
    try:
        values.remove(item)
    except ValueError:
        break
    if item != ".":
        zipped.append(item)
    else:
        for x in reversed(values):
            if x != ".":
                zipped.append(x)
                values.remove(x)
                break

print(sum(idx * val for idx, val in enumerate(zipped)))
