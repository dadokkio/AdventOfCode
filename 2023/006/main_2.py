with open("input.txt") as f:
    data = f.readlines()
    time_f = int("".join([x for x in data[0].split(": ")[-1].split()]))
    distance = int("".join([x for x in data[1].split(": ")[-1].split()]))


wins = sum([1 for time in range(time_f, 0, -1) if time * (time_f - time) > distance])
print(wins)
