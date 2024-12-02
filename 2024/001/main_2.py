inp = open("input.txt", "r").read().strip().split()
a = sorted([int(inp[x]) for x in range(len(inp)) if x % 2 == 0])
b = sorted([int(inp[x]) for x in range(len(inp)) if x % 2 == 1])

print(sum(a[i] * b.count(a[i]) for i in range(len(a))))
