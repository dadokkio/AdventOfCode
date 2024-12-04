data = [
    list(line)
    for line in open("/home/dadokkio/Docker/aoc/2024/004/input.txt", "r").readlines()
]

directions = [
    (1, 1),  # down-right diagonal
    (-1, -1),  # up-left diagonal
    (-1, 1),  # up-right diagonal
    (1, -1),  # down-left diagonal
]

dir_letter = ["↘️", "↖️", "↗️", "↙️"]

opposite = {
    (1, -1): (1, 1),
    (-1, +1): (-1, -1),
    (1, 1): (-1, 1),
    (-1, -1): (1, -1),
}

letters = ["M", "A", "S"]

xmas = 0

for line_idx, line in enumerate(data):
    for column_idx, letter in enumerate(line):
        if letter == letters[0]:
            for id_idx, dir in enumerate(directions):
                ok = False
                letter_id = 0
                print(
                    f"{line_idx:03}-{column_idx:03} {dir_letter[id_idx]}  {letter}",
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
                        a = data[x - dir[0] * 2][y - dir[1] * 2]
                        new_dir = opposite[dir]
                        one = data[x - dir[0] * 2 + new_dir[0]][
                            y - dir[1] * 2 + new_dir[1]
                        ]
                        two = data[x - dir[0] * 2 - new_dir[0]][
                            y - dir[1] * 2 - new_dir[1]
                        ]
                        if f"{one}{a}{two}" in ["MAS", "SAM"]:
                            xmas += 1
                            print(f" {one}{a}{two} \t**OK**")
                        else:
                            print(f"* {one}{a}{two} \t**NOPE**")
                        ok = True
                        break

                    if not (0 <= x < len(data) and 0 <= y <= len(line) - 1):
                        print("*", end="")
                        break

                    if not ok:
                        print(data[x][y], end="")
                        letter_id += 1
                if not ok:
                    print(" \t\tNO")

print(xmas // 2)
