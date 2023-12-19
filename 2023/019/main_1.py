data = open("input.txt").read().split("\n\n")

rules = {}

for l in data[0].splitlines():
    name, rule = l.split("{")
    rules[name] = rule[:-1].split(",")

total = 0
for p in data[1].splitlines():
    state = "in"
    conds = {c.split("=")[0]: int(c.split("=")[1]) for c in p[1:-1].split(",")}
    while state not in ("A", "R"):
        current_cond = rules[state]
        for step in current_cond:
            if ":" in step:
                cond, next_cond = step.split(":")
                if eval(f'conds["{cond[0]}"]' + "".join(cond[1:])):
                    state = next_cond
                    break
            else:
                state = step

        if state == "A":
            total += sum(conds.values())
            break
        elif state == "R":
            break

print(total)
