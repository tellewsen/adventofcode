import numpy as np


def read_file(filename):
    with open(filename, "r") as f:
        lines = [line.rstrip() for line in f.readlines()]
    char_map = {}
    for line in lines[2:]:
        key, value = line.split(" -> ")
        char_map[key] = value
    return char_map, lines[0]


def go_once(char_map, line):
    new_line = line[0]
    for i in range(1, len(line)):
        chars = line[i - 1] + line[i]
        if chars in char_map:
            new_line += char_map[chars] + line[i]
        else:
            new_line += chars
    return new_line


def p1(char_map, line):
    # bruto force lol
    new_line = line
    for i in range(10):
        print("gone ", i, " steps")
        new_line = go_once(char_map, new_line)
    counts = {}
    for c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        count = new_line.count(c)
        if count:
            counts[c] = count
    print(counts[max(counts, key=counts.get)] - counts[min(counts, key=counts.get)])


def p2(char_map, line):
    """Do it the smart? way"""
    # initialize
    counts = {k: 0 for k in char_map}
    for i in range(1, len(line)):
        chars = line[i - 1] + line[i]
        if chars in char_map:
            counts[chars] += 1
        else:
            counts[chars] = 1
    # step through and keep count
    for _ in range(40):
        for k, v in counts.copy().items():
            if v == 0:
                continue
            extra_char = char_map[k]
            counts[k] -= v  # we lose the current pair
            counts[k[0] + extra_char] += v  # the new left pair
            counts[extra_char + k[1]] += v  # the new right pair
    # Count characters
    char_counts = {}
    for k, v in counts.items():
        if k[0] in char_counts:
            char_counts[k[0]] += v
        else:
            char_counts[k[0]] = v
        if k[1] in char_counts:
            char_counts[k[1]] += v
        else:
            char_counts[k[1]] = v
    # round after division to account for edgecharacters
    char_counts = {k: round(v / 2) for k, v in char_counts.items()}
    print(
        char_counts[max(char_counts, key=char_counts.get)]
        - char_counts[min(char_counts, key=char_counts.get)]
    )


def main():
    filenames = [
        "ex.txt",
        "input.txt",
    ]
    for name in filenames:
        char_map, line = read_file(name)
        # p1(char_map, line)
        p2(char_map, line)


main()
