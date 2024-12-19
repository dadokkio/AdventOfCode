from functools import lru_cache


@lru_cache(None)
def contains_pattern(word):
    if not word:
        return True
    return any(
        word.startswith(start) and contains_pattern(word[len(start) :])
        for start in patterns
    )


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        patterns = sorted(
            f.readline()[:-1].split(", "), key=lambda x: len(x), reverse=True
        )
        words = [x.strip() for x in f.readlines()[1:]]
    print(sum(contains_pattern(word) for word in words))
