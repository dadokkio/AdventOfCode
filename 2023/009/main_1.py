tot = 0

with open("input.txt", "r") as f:
    for line in f.readlines():
        numbers = [int(n) for n in line.split()]
        print(numbers)
        lasts = [numbers[-1]]
        others = numbers
        while all(i == 0 for i in others) == False:
            for i in range(len(others) - 1):
                others[i] = others[i + 1] - others[i]
            del others[-1]
            lasts.append(others[-1])
            print("\t", others)
        print(sum(lasts))
        tot += sum(lasts)

print(tot)
