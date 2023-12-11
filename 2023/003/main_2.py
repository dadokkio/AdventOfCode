total = 0
info = {}

stars = {}

with open("input.txt", "r") as f:
    data = f.readlines()
    for line in range(len(data)):
        info[line] = []
        last = -1
        for char in range(len(data[line])):
            no = ""
            if char > last and data[line][char].isdigit():
                start = char - 1
                while data[line][char].isdigit():
                    no += data[line][char]
                    char += 1
                last = char - 1
                info[line].append((int(no), start, char))

    for line in info:
        items = []
        for no, start, end in info[line]:
            ok = False
            for i in range(start, end + 1):
                if line > 0 and data[line - 1][i] == "*":
                    ok = True
                    stars.setdefault((line - 1, i), [])
                    stars[(line - 1, i)].append(no)
                    break
                if line < len(data) - 1 and data[line + 1][i] == "*":
                    ok = True
                    stars.setdefault((line + 1, i), [])
                    stars[(line + 1, i)].append(no)
                    break
            if not ok and (start > 0 and data[line][start] == "*"):
                stars.setdefault((line, start), [])
                stars[(line, start)].append(no)
                ok = True
            if not ok and (end < len(data[line]) and data[line][end] == "*"):
                stars.setdefault((line, end), [])
                stars[(line, end)].append(no)
                ok = True

    for info, nos in stars.items():
        if len(nos) == 2:
            total += nos[0] * nos[1]

print(total)
