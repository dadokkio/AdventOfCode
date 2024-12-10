from itertools import product

with open("/home/dadokkio/Docker/aoc/2024/007/input.txt", "r") as f:
    data = {
        int(line.split(":")[0]): [int(x) for x in line.split(":")[1].split()]
        for line in f
    }

all_valid = 0
for res, no in data.items():
    for iter_operation in product("*+|", repeat=len(no) - 1):
        tot = no[0]
        for number, operation in zip(no[1:], iter_operation):
            if operation == "*":
                tot *= number
            elif operation == "+":
                tot += number
            else:
                tot = int(f"{tot}{number}")
        if tot == res:
            all_valid += res
            break

print(all_valid)
