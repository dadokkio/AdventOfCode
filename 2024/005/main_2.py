from itertools import combinations
from main_1 import parse_lines


def flip(update, rules):
    for a, b in combinations(update, 2):
        if (b, a) in rules:
            idx1, idx2 = update.index(a), update.index(b)
            update[idx1], update[idx2] = update[idx2], update[idx1]
            break


def align_to_rules(update, rules):
    while any((b, a) in rules for a, b in combinations(update, 2)):
        flip(update, rules)
    return update


if __name__ == "__main__":
    rules, updates = parse_lines()
    not_aligned_updates = [
        align_to_rules(update, rules)
        for update in updates
        if any((b, a) in rules for a, b in combinations(update, 2))
    ]
    middle_numbers = [update[len(update) // 2] for update in not_aligned_updates]
    print(sum(middle_numbers))
