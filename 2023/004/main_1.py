tot = 0

with open("input.txt", "r") as f:
    for line in f.readlines():
        res = 0
        others, mine = line.split("|")
        card, others = others.split(":")
        card = int(card.split(" ")[-1])
        mine = [int(x.strip()) for x in mine.split(" ") if x != ""]
        others = [int(x.strip()) for x in others.split(" ") if x != ""]
        no = len([x for x in mine if x in others])
        if no > 0:
            res = 1
            for i in range(no - 1):
                res *= 2
        else:
            res = 0
        tot += res

print(tot)
