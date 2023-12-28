from math import inf


def make_maps(lines):
    maps = {}
    for line in lines:
        name, numbers = line.split(":")
        if name == "seeds":
            maps[name] = [int(i) for i in numbers.lstrip().split()]
            continue
        ranges = numbers.rstrip("\n").lstrip("\n").split("\n")
        maps[name] = []
        for rang in ranges:
            dest, start, count = rang.split()
            maps[name].append((int(dest), int(start), int(count)))
    return maps


def map_from_to(map_id, mapping):
    for map in mapping:
        dest, start, count = map
        if start <= map_id <= start + count:
            return dest - start + map_id
    return map_id


def seed2loc(seed_id: int, mappings):
    seed_id = map_from_to(seed_id, mappings["seed-to-soil map"])
    seed_id = map_from_to(seed_id, mappings["soil-to-fertilizer map"])
    seed_id = map_from_to(seed_id, mappings["fertilizer-to-water map"])
    seed_id = map_from_to(seed_id, mappings["water-to-light map"])
    seed_id = map_from_to(seed_id, mappings["light-to-temperature map"])
    seed_id = map_from_to(seed_id, mappings["temperature-to-humidity map"])
    seed_id = map_from_to(seed_id, mappings["humidity-to-location map"])
    return seed_id


def part1(lines):
    mappings = make_maps(lines)
    locs = set()
    for seed in mappings["seeds"]:
        locs.add(seed2loc(seed, mappings))
    return min(locs)


def seed_at_location(location) -> bool:
    return


def part2(lines):
    mappings = make_maps(lines)
    best = inf
    location = 0
    while True:
        if seed_at_location(location):
            return location
            break
    #     location += 1
    # for i in range(0, len(mappings["seeds"]), 2):
    #     start = mappings["seeds"][i]
    #     count = mappings["seeds"][i + 1]
    #     print(i)
    #     for j in range(start, start + count):
    #         loc = seed2loc(j, mappings)
    #         if loc < best:
    #             print("new best ", best)
    #             best = loc
    # return best


if __name__ == "__main__":
    with open("input") as f:
        lines = f.read().split("\n\n")

    print("p1: ", part1(lines))
    print("p2: ", part2(lines))
