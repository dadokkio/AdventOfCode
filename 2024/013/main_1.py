import pathlib
import re

data = pathlib.Path("./input.txt").read_text()
runs = [
    {
        "c1": int(re.findall(r"\+(\d+)", button_a)[0]),
        "c2": int(re.findall(r"\+(\d+)", button_b)[0]),
        "c3": int(re.findall(r"=(\d+)", prize)[0]),
        "c4": int(re.findall(r"\+(\d+)", button_a)[1]),
        "c5": int(re.findall(r"\+(\d+)", button_b)[1]),
        "c6": int(re.findall(r"=(\d+)", prize)[1]),
    }
    for button_a, button_b, prize in (
        block.split("\n") for block in data.strip().split("\n\n")
    )
]
total = 0
for run in runs:
    c1, c2, c3, c4, c5, c6 = run.values()

    b = (c1 * c6 - c4 * c3) / (c1 * c5 - c4 * c2)
    a = (c3 - c2 * b) / c1

    if a.is_integer() and b.is_integer():
        total += a * 3 + b
print(int(total))
