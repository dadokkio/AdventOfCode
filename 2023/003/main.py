total = 0
info = {}

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
                if (
                    line > 0
                    and not data[line - 1][i].isdigit()
                    and data[line - 1][i] not in [".", "\n"]
                ) or (
                    line < len(data) - 1
                    and not data[line + 1][i].isdigit()
                    and data[line + 1][i] not in [".", "\n"]
                ):
                    ok = True
                    break
            if not ok and (
                (
                    start > 0
                    and not data[line][start].isdigit()
                    and data[line][start] not in [".", "\n"]
                )
                or (
                    end < len(data[line])
                    and not data[line][end].isdigit()
                    and data[line][end] not in [".", "\n"]
                )
            ):
                ok = True
            if ok == True:
                total += no

print(total)
