from collections import Counter

info = {}

bids_ranks = ["5", "14", "23", "113", "122", "1112", "11111"]
FACE_CARDS = {
    "2": "2",
    "3": "3",
    "4": "4",
    "5": "5",
    "6": "6",
    "7": "7",
    "8": "8",
    "9": "9",
    "T": "A",
    "J": "1",
    "Q": "C",
    "K": "D",
    "A": "E",
}


with open("input.txt") as f:
    for line in f.readlines():
        hand, bid = line.split(" ")
        call = "".join([str(x) for x in sorted(Counter(hand).values())])

        no_j = Counter(hand)["J"]
        top_noj = Counter(hand.replace("J", "")).most_common(1)

        if top_noj:
            new_hand = hand.replace("J", top_noj[0][0])
            new_call = "".join([str(x) for x in sorted(Counter(new_hand).values())])
        else:
            new_hand = hand
            new_call = "5"

        info.setdefault(new_call, []).append(
            {
                "bid": int(bid),
                "value": [FACE_CARDS[x] for x in hand],
                "orig": hand,
                "new": new_hand or None,
            }
        )

rank = 1
total = 0
for bids_rank in reversed(bids_ranks):
    print(bids_rank)
    for bid in sorted(info[bids_rank], key=lambda x: x["value"]):
        print(
            "\t",
            "".join(bid["value"]),
            bid["orig"],
            bid["new"],
            f"{rank} * {bid['bid']}",
        )
        total += rank * bid["bid"]
        rank += 1

print(total)

# 249949357
# 249781879
