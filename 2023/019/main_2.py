from copy import deepcopy

data = open("input.txt").read().split("\n\n")

rules = {}

for l in data[0].splitlines():
    name, rule = l.split("{")
    rules[name] = rule[:-1].split(",")


def process(state, rules, ranges=None):
    if ranges is None:
        ranges = {"x": (1, 4000), "m": (1, 4000), "a": (1, 4000), "s": (1, 4000)}
    if state == "A":
        return (
            (ranges["x"][1] - ranges["x"][0] + 1)
            * (ranges["m"][1] - ranges["m"][0] + 1)
            * (ranges["a"][1] - ranges["a"][0] + 1)
            * (ranges["s"][1] - ranges["s"][0] + 1)
        )

    elif state == "R":
        return 0
    total = 0
    for step in rules[state]:
        if ":" not in step:
            total += process(step, rules, ranges)
        else:
            cond, next_cond = step.split(":")
            new_range = deepcopy(ranges)

            cond_value = int(cond[2:])
            step_range = ranges[cond[0]]

            if step_range[0] < cond_value < step_range[1]:
                new_range[cond[0]] = (
                    (step_range[0], cond_value - 1)
                    if cond[1] == "<"
                    else (cond_value + 1, step_range[1])
                )
                ranges[cond[0]] = (
                    (cond_value, step_range[1])
                    if cond[1] == "<"
                    else (step_range[0], cond_value)
                )
                total += process(next_cond, rules, new_range)
    return total


print(process("in", rules))
