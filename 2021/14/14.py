import numpy as np


def read_file(filename):
    with open(filename, "r") as f:
        lines = [line.rstrip() for line in f.readlines()]
    char_map = {}
    for line in lines[2:]:
        key, value = line.split(" -> ")
        char_map[key] = value
    return char_map, lines[0]


def main():
    filenames = [
        "ex.txt",
        "input.txt",
    ]
    for name in filenames:
        temp, line = read_file(name)
    print(temp, line)


main()
