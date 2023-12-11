tot = 0

with open("input.txt", "r") as f:
    data = f.readlines()
    card_plus = {x + 1: {"count": 1, "score": 0} for x in range(len(data))}
    for line in data:
        res = 0
        others, mine = line.split("|")
        card, others = others.split(":")
        card = int(card.split(" ")[-1])
        mine = [int(x.strip()) for x in mine.split(" ") if x != ""]
        others = [int(x.strip()) for x in others.split(" ") if x != ""]
        no = len([x for x in mine if x in others])
        card_plus[card]["score"] = no

        for i in range(card_plus[card]["count"]):
            for i in range(no):
                card_plus[card + i + 1]["count"] += 1


for card, info in card_plus.items():
    tot += info["count"]

print(card_plus)
print(tot)
# 6283755
