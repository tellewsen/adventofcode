import numpy as np
import functools


def read_file(filename):
    with open(filename, "r") as f:
        data = [i.rstrip() for i in f.readlines()]
    return data


POINT_MAP = {")": 3, "]": 57, "}": 1197, ">": 25137}
open_char = {"(": ")", "[": "]", "{": "}", "<": ">"}
close_char = {v: k for k, v in open_char.items()}
POINT_MAP2 = {")": 1, "]": 2, "}": 3, ">": 4}


def get_first_illegal_char(line):
    waiting_for = []
    for char in line:
        if char in open_char.keys():  # opening char
            waiting_for.append(char)
        else:  # closing_char
            if waiting_for[-1] == close_char[char]:
                waiting_for.pop()
            else:
                return char


def p1(hm):
    illegal_chars = []
    for line in hm:
        illegal_char = get_first_illegal_char(line)
        if illegal_char:
            illegal_chars.append(illegal_char)
    return sum([POINT_MAP[i] for i in illegal_chars])


def get_missing_chars(line):
    waiting_for = []
    for char in line:
        if char in open_char.keys():  # opening char
            waiting_for.append(char)
        else:  # closing_char
            waiting_for.pop()
    return ''.join([open_char[i] for i in reversed(waiting_for)])


def calculate_score(chars):
    score = 0
    for char in chars:
        score *= 5
        score += POINT_MAP2[char]
    return score


def p2(content):
    incomplete = [i for i in content if not get_first_illegal_char(i)]
    missing_chars = [get_missing_chars(i) for i in incomplete]
    scores = [calculate_score(i) for i in missing_chars]
    mid = round(len(scores)/2)
    print(scores)
    return sorted(scores)[mid]


def main():
    filename = "input.txt"
    #filename = "example_input.txt"
    hm = read_file(filename)
    print(1, p1(hm))
    print(2, p2(hm))


if __name__ == "__main__":
    main()
