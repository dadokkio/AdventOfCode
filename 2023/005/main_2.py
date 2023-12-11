from tqdm import tqdm

info = {}
all_seeds = []

with open("input.txt", "r") as f:
    data = f.readlines()
    seeds = [int(x.strip()) for x in data[0].split(": ")[-1].split()]
    for i in tqdm(range(0, len(seeds) // 2, 2)):
        for j in range(seeds[i * 2], seeds[i * 2] + seeds[i * 2 + 1] + 1):
            all_seeds.append(j)

    index = 1

    for line in data[index:]:
        if line.find("map:") != -1:
            topic = line.split()[0]
            info[topic] = {"from": topic.split("-")[0], "to": topic.split("-")[-1]}
            info[topic]["items"] = []
        elif line.strip() != "":
            no = [int(x.strip()) for x in line.split()]
            info[topic]["items"].append(no)
        index += 1


location_min = 1000000000000

for seed in tqdm(all_seeds):
    what = "seed"
    jump = seed
    while what != "location":
        for topic in info.keys():
            if info[topic]["from"] == what:
                for ranges in info[topic]["items"]:
                    if jump in range(ranges[1], ranges[1] + ranges[2]):
                        jump = jump - ranges[1] + ranges[0]
                        break

                what = info[topic]["to"]
                break
    if jump < location_min:
        location_min = jump

print(location_min)
