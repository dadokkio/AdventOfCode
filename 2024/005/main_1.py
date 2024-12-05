from itertools import combinations


def parse_lines(filename="input.txt"):
    with open(filename) as file:
        rules = set()
        updates = []
        for line in file:
            line = line.strip()
            if "|" in line:
                rules.add(tuple(map(int, line.split("|"))))
            elif "," in line:
                updates.append(list(map(int, line.split(","))))
    return rules, updates


if __name__ == "__main__":
    rules, updates = parse_lines()
    middle_numbers = [
        update[len(update) // 2]
        for update in updates
        if all((b, a) not in rules for a, b in combinations(update, 2))
    ]
    print(sum(middle_numbers))
