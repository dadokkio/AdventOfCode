inp = open("input.txt", "r").read().strip().split()

a = sorted([int(inp[x]) for x in range(len(inp)) if x % 2 == 0])
b = sorted([int(inp[x]) for x in range(len(inp)) if x % 2 == 1])

print(sum(abs(a[i] - b[i]) for i in range(len(a))))
