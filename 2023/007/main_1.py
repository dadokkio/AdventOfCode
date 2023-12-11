from collections import Counter
from pprint import pprint

info = {}

bids_ranks = ["5", "14", "23", "113", "122", "1112", "11111"]
FACE_CARDS = {
    "2": "O",
    "3": "N",
    "4": "M",
    "5": "L",
    "6": "I",
    "7": "H",
    "8": "G",
    "9": "F",
    "T": "E",
    "J": "D",
    "Q": "C",
    "K": "B",
    "A": "A",
}


with open("input.txt") as f:
    for line in f.readlines():
        hand, bid = line.split(" ")
        call = "".join([str(x) for x in sorted(Counter(hand).values())])
        info.setdefault(str(call), []).append(
            {"bid": int(bid), "value": [FACE_CARDS[x] for x in hand], "orig": hand}
        )

rank = 1
total = 0
for bids_rank in reversed(bids_ranks):
    print(bids_rank)
    for bid in sorted(info[bids_rank], key=lambda x: x["value"], reverse=True):
        print("\t", bid["value"], bid["orig"], rank)
        bid["rank"] = rank
        total += rank * bid["bid"]
        rank += 1

print(total)
