total = 0
total_2 = 0
max = {"red": 12, "green": 13, "blue": 14}
ok = True

games = {}

with open("input.txt", "r") as f:
    for line in f.readlines():
        games[line] = {"red": 0, "green": 0, "blue": 0}
        game, results = line.split(":")
        game = int(game.split(" ")[-1])
        results = [x.split() for x in results.replace(";", ",").split(",")]
        ok = True
        for value, color in results:
            if int(value) > games[line][color]:
                games[line][color] = int(value)
            if int(value) > max[color]:
                ok = False
                continue
        if ok:
            total += game

    for item in games:
        total_2 += games[item]["red"] * games[item]["green"] * games[item]["blue"]


print(total)
print(total_2)
