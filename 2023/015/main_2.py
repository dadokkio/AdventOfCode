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


boxes = {}
for instruction in data:
    if "=" in instruction:
        new_data = instruction.split("=")
        no = get_hash_value(new_data[0])
        if no in boxes:
            if existing_lens := [
                boxes[no].index(lens) for lens in boxes[no] if new_data[0] in lens
            ]:
                boxes[no][existing_lens[0]] = new_data
            else:
                boxes[no] += [new_data]
        else:
            boxes[no] = [new_data]

    elif "-" in instruction:
        label = instruction[:-1]
        no = get_hash_value(label)
        if no in boxes:
            boxes[no] = [lens for lens in boxes[no] if label not in lens]


focusing_power = 0
for key, value in boxes.items():
    if len(value) != 0:
        for i, lens in enumerate(value):
            focusing_power += (key + 1) * (i + 1) * int(lens[1])

print(focusing_power)
