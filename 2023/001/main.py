total = 0

numbers = [
    "zero",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
]

with open("input.txt", "r") as f:
    for line in f.readlines():
        for no_str, no in zip(numbers, range(10)):
            repl = no_str[:-1] + str(no) + no_str[-1]
            line = line.replace(no_str, repl)
        l_numbers = [int(char) for char in line if char.isdigit()]
        total += int(f"{l_numbers[0]}{l_numbers[-1]}")

print(total)
