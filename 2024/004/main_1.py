data = [list(line) for line in open("input.txt", "r").readlines()]

directions = [
    (0, 1),  # right
    (0, -1),  # left
    (1, 0),  # down
    (-1, 0),  # up
    (1, 1),  # down-right
    (-1, -1),  # up-left
    (1, -1),  # down-left
    (-1, 1),  # up-right
]

dir_letter = ["➡️", "⬅️", "⬇️", "⬆️", "↘️", "↖️", "↗️", "↙️"]

letters = ["X", "M", "A", "S"]

xmas = 0

for line_idx, line in enumerate(data):
    for column_idx, letter in enumerate(line):
        if letter == letters[0]:
            for dir_idx, dir in enumerate(directions):
                ok = False
                letter_id = 0
                print(
                    f"{line_idx:03}-{column_idx:03} {dir_letter[dir_idx]}  {letter}",
                    end="",
                )
                x, y = line_idx, column_idx
                while data[x][y] == letters[letter_id]:
                    x = x + dir[0]
                    y = y + dir[1]

                    if (
                        data[x - dir[0]][y - dir[1]] == letters[-1]
                        and letter_id == len(letters) - 1
                    ):
                        xmas += 1
                        ok = True
                        print(" \t**OK**")
                        break

                    if not (0 <= x < len(data) and 0 <= y <= len(line) - 1):
                        print("*", end="")
                        break

                    if not ok:
                        print(data[x][y], end="")
                        letter_id += 1
                if not ok:
                    print("    \tNO")

print(f"\nTOTAL: {xmas}")
