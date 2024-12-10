couples = []

with open("/home/dadokkio/Docker/aoc/2024/009/input.txt", "r") as f:
    data = f.read()
    for idx, x in enumerate(range(len(data) // 2)):
        couples.extend(
            (
                [idx for _ in range(int(data[x * 2]))],
                ["." for _ in range(int(data[x * 2 + 1]))],
            )
        )
    if len(data) % 2 != 0:
        couples.append([idx + 1 for _ in range(int(data[-1]))])

a = len(couples)

values = couples.copy()
for idx, item in enumerate(reversed(values[1:])):
    if idx % 2 == 1:
        continue
    if idx % 100 == 0:
        print(f"{idx}/{a}")
    many = len(item)
    for idy, dotted in enumerate(couples[: len(couples) - idx - 1]):
        if "." not in dotted:
            continue
        if len(values) - idx + 1 < idy:
            continue
        dot_no = len([x for x in dotted if x == "."])
        if dot_no >= many:
            replaced = 0
            for idz in range(len(couples[idy])):
                if replaced == many:
                    break
                if couples[idy][idz] == ".":
                    couples[idy][idz] = item[0]
                    replaced += 1
            couples[len(couples) - idx - 1] = ["."] * many
            break

index = 0
total = 0

with open("out.txt", "w") as f:
    for i in couples:
        f.write(str(i) + "\n")
        for item in i:
            if item != ".":
                total += index * item
            index += 1
print(total)
