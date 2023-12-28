import re


def test_main():
    with open("./example_input") as f:
        lines = f.readlines()

    assert part1(lines) == 288
    assert part2(lines) == 71503


def part1(lines):
    time = [int(i) for i in re.findall(r"\d+", lines[0])]
    dist = [int(i) for i in re.findall(r"\d+", lines[1])]
    tot_combinations = 1
    for t, d in zip(time, dist):
        combs = 0
        for i in range(1, t - 1):  # can be optimized
            if i * (t - i) > d:
                combs += 1
        tot_combinations *= combs
    return tot_combinations


def part2(lines):
    t = int("".join(re.findall(r"\d+", lines[0])))
    d = int("".join(re.findall(r"\d+", lines[1])))
    for i in range(t):
        if i * (t - i) > d:
            lowest = i
            break
    for j in range(t, 0, -1):
        if j * (t - j) > d:
            highest = j
            break
    return highest - lowest + 1


def main():
    with open("./input") as f:
        lines = f.readlines()
    print("p1: ", part1(lines))
    print("p2: ", part2(lines))


if __name__ == "__main__":
    main()
