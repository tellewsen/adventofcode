import math


def read_file(filename):
    with open(filename, "r") as f:
        data = [i.rstrip() for i in f.readlines()]
    return data


OPEN2CLOSE = {"(": ")", "[": "]", "{": "}", "<": ">"}


def get_first_illegal_char(line):
    waiting_for = []
    for char in line:
        if char in OPEN2CLOSE:  # opening char
            waiting_for.append(char)
        else:  # closing_char
            if char == OPEN2CLOSE[waiting_for[-1]]:
                waiting_for.pop()
            else:
                return char


def p1(lines):
    point_map = {")": 3, "]": 57, "}": 1197, ">": 25137}
    illegal_chars = []
    for line in lines:
        illegal_char = get_first_illegal_char(line)
        if illegal_char:
            illegal_chars.append(illegal_char)
    return sum([point_map[i] for i in illegal_chars])


def get_missing_chars(line):
    waiting_for = []
    for char in line:
        if char in OPEN2CLOSE.keys():  # opening char
            waiting_for.append(char)
        else:  # closing_char
            waiting_for.pop()
    return "".join([OPEN2CLOSE[i] for i in reversed(waiting_for)])


def calculate_score(chars):
    point_map = {")": 1, "]": 2, "}": 3, ">": 4}
    score = 0
    for char in chars:
        score *= 5
        score += point_map[char]
    return score


def p2(content):
    incomplete = [i for i in content if not get_first_illegal_char(i)]
    missing_chars = [get_missing_chars(i) for i in incomplete]
    scores = [calculate_score(i) for i in missing_chars]
    mid = math.floor(len(scores) / 2)
    return sorted(scores)[mid]


def main():
    lines = read_file("input.txt")
    print(1, p1(lines))
    print(2, p2(lines))


if __name__ == "__main__":
    main()
