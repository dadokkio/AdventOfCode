total = 0

with open("input.txt", "r") as f:
    for line in f.readlines():
        l_numbers = [int(char) for char in line if char.isdigit()]
        total += int(f"{l_numbers[0]}{l_numbers[-1]}")

print(total)
