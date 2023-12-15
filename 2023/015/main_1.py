with open("input.txt") as file:
    data = file.read().strip().split(",")


def get_hash_value(string):
    return (
        sum(
            (ord(char)) * (17 ** (len(string) - i)) % 256
            for i, char in enumerate(string)
        )
        % 256
    )


print(sum(get_hash_value(string) for string in data))
