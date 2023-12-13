import numpy as np

inputs = []

with open("input.txt") as f:
    single = []
    for line in f:
        if line.strip() == "":
            inputs.append(single)
            single = []
        else:
            single.append(line.strip())
    inputs.append(single)

totals = []


def match(s1, s2):
    ok = False
    for c1, c2 in zip(s1, s2):
        if c1 != c2:
            if ok:
                return False
            else:
                ok = True
    return ok


for index, input_data in enumerate(inputs):
    for type, data in [
        ("row", np.array([list(x) for x in input_data])),
        ("col", np.array([list(x) for x in input_data]).T),
    ]:
        if len(totals) == index + 1:
            continue
        print(f"checking {index} {type}")
        for row in range(len(data)):
            c = start = row
            end = row + 1
            ok = start >= 0 and start < len(data) - 1 and end <= len(data)
            changes = False
            print(f"\tchecking {row}")
            while start >= 0 and end < len(data):
                print(f"\t\tstart {start} - end {end}", end=" ")
                smudge = match("".join(data[start]), "".join(data[end]))
                if "".join(data[start]) != "".join(data[end]) or (
                    not changes and smudge
                ):
                    if not changes and smudge:
                        print("-> ok updated*")
                        start -= 1
                        end += 1
                        changes = True
                        continue
                    print("-> no match exiting")
                    ok = False
                    break
                else:
                    print("-> ok")
                start -= 1
                end += 1
            if ok and changes:
                print(f"\t\t\tfound {c} {type}")
                totals.append((c + 1, type))
                break

print(sum(val * 100 if type == "row" else val for val, type in totals))
