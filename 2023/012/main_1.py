def gen_arr(text, options):
    if not text:
        return 0 if options else 1
    if text.startswith("."):
        return gen_arr(text.strip("."), options)
    if text.startswith("?"):
        return gen_arr(text.replace("?", ".", 1), options) + gen_arr(
            text.replace("?", "#", 1), options
        )
    if text.startswith("#"):
        if not options:
            return 0
        if len(text) < options[0]:
            return 0
        if any(c == "." for c in text[: options[0]]):
            return 0
        if len(options) <= 1:
            return gen_arr(text[options[0] :], options[1:])
        if len(text) < options[0] + 1 or text[options[0]] == "#":
            return 0
        return gen_arr(text[options[0] + 1 :], options[1:])
    raise Exception("no other branches possible")


with open("test.txt") as input_file:
    input_lines = input_file.readlines()
    input_lines = [line.strip("\n") for line in input_lines]
    totals = 0
    for line in input_lines:
        text, options = line.split(" ")
        options = tuple(int(x) for x in options.split(","))
        totals += gen_arr(text, options)
    print(totals)
