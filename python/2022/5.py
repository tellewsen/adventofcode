import re


def make_stacks():
    stacks = [[] for _ in range(9)]
    for i in range(7, -1, -1):
        for j in range(1, 36, 4):
            if read[i][j] != " ":
                stacks[(j // 4)].append(read[i][j])
    return stacks


def p1(stacks):
    for line in read[10:]:
        num, start, end = map(
            int, re.match(r"move (\d+) from (\d+) to (\d+)", line).groups()
        )
        for _ in range(num):
            stacks[end - 1].append(stacks[start - 1].pop())
    print("".join(i[-1] for i in stacks))


def p2(stacks):
    for line in read[10:]:
        num, start, end = map(
            int, re.match(r"move (\d+) from (\d+) to (\d+)", line).groups()
        )
        boxes = stacks[start - 1][-num:]
        stacks[end - 1].extend(boxes)
        stacks[start - 1] = stacks[start - 1][:-num]
    print("".join(i[-1] for i in stacks))


with open("input") as f:
    read = f.read().splitlines()


p1(make_stacks())
p2(make_stacks())
