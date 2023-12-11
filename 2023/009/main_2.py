tot = 0

with open("input.txt", "r") as f:
    for line in f.readlines():
        numbers = [int(n) for n in line.split()]
        print(numbers)
        lasts = [numbers[0]]
        others = numbers
        while all(i == 0 for i in others) == False:
            for i in range(len(others) - 1):
                others[i] = others[i + 1] - others[i]
            del others[-1]
            lasts.append(others[0])
            print("\t", others)
        odd = sum([lasts[x] for x in range(len(lasts)) if x % 2 == 0])
        even = sum([lasts[x] for x in range(len(lasts)) if x % 2 == 1])
        tot += odd - even
        print(lasts, (odd - even))

print(tot)
