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
            print(f"\tchecking {row}")
            while start >= 0 and end < len(data):
                print(f"\t\tstart {start} - end {end}", end=" ")
                if "".join(data[start]) != "".join(data[end]):
                    print("-> no match exiting")
                    ok = False
                    break
                else:
                    print("-> ok")
                start -= 1
                end += 1
            if ok:
                print(f"\t\t\tfound {c} {type}")
                totals.append((c + 1, type))
                break

print(sum(val * 100 if type == "row" else val for val, type in totals))
