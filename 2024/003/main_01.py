import re

data = open("input.txt", "r").read()

regex = r"mul\((\d+),(\d+)\)"
matches = re.findall(regex, data)

tot = 0
for match in matches:
    num1, num2 = match
    tot += int(num1) * int(num2)

print(tot)
