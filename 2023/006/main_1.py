with open("input.txt") as f:
    data = f.readlines()
    times = [int(x) for x in data[0].split(": ")[-1].split()]
    distances = [int(x) for x in data[1].split(": ")[-1].split()]


def multiplyList(myList):
    result = 1
    for x in myList:
        result = result * x
    return result


wins = []
for items in zip(times, distances):
    wins.append(
        sum(
            [
                1
                for time in range(items[0], 0, -1)
                if time * (items[0] - time) > items[1]
            ]
        )
    )

print(multiplyList(wins))
