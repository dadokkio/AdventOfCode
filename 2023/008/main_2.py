info = {}

with open("input.txt", "r") as f:
    instructions = [x for x in f.readline().strip()]

    data = f.readlines()
    for item in data[1:]:
        now = item.split("=")[0].strip()
        left, right = item.split("(")[1].split(")")[0].split(", ")
        info[now] = [left, right]

starts = [x for x in info if x.endswith("A")]
count = 1

while len([x for x in starts if x.endswith("Z")]) != len(starts):
    for instruction in instructions:
        starts = [
            info[start][0] if instruction == "L" else info[start][1] for start in starts
        ]
        if len([x for x in starts if x.endswith("Z")]) == len(starts):
            break
        else:
            count += 1

print(count)

# 18024643846273
# 48648322148.2
#     8245000
