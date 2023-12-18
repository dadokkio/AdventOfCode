from main_1 import count

data = open("input.txt").read().split()

max_en = 0
for y in range(len(data)):
    en_sx = count(0, y, +1, 0)
    en_dx = count(len(data[0]) - 1, y, -1, 0)
    max_en = max(max_en, en_sx, en_dx)

for x in range(len(data[0])):
    en_top = count(x, 0, 0, +1)
    en_bottom = count(x, len(data) - 1, 0, -1)
    max_en = max(max_en, en_top, en_bottom)

print(max_en)
