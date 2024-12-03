import re

data = open("input.txt", "r").read()
regex = r"mul\((\d+),(\d+)\)"

tot = 0
parts = data.split("don't()")
for idx, x in enumerate(parts):
    text = x if idx in [0, len(parts)] else "".join(x.split("do()")[1:])
    matches = re.findall(regex, text)
    for match in matches:
        num1, num2 = match
        tot += int(num1) * int(num2)
print(tot)
