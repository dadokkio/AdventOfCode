info = {}

with open("input.txt", "r") as f:
    instructions = [x for x in f.readline().strip()]

    data = f.readlines()
    for item in data[1:]:
        now = item.split("=")[0].strip()
        left, right = item.split("(")[1].split(")")[0].split(", ")
        info[now] = [left, right]


start = "AAA"
count = 1

while start != "ZZZ":
    for instruction in instructions:
        start = info[start][0] if instruction == "L" else info[start][1]
        if start == "ZZZ":
            break
        else:
            print(start)
            count += 1

print(count)
