# Regex garbage
import re


def solver(text):
    matches = re.findall(r"mul\(\d+,\d+\)", text)
    p1 = 0
    for m in matches:
        g = m.split(",")
        res = int(g[0][4:]) * int(g[1][:-1])
        p1 += res

    mul_enabled = True
    p2 = 0
    instructions = re.findall(r"mul\((\d+),(\d+)\)|(do\(\))|(don\'t\(\))", text)
    for part in instructions:
        if part[0] == "":
            if part[2] == "do()":
                mul_enabled = True
            elif part[3] == "don't()":
                mul_enabled = False
        elif part[0] != "":
            x, y = int(part[0]), int(part[1])
            if mul_enabled:
                p2 += x * y
    return p1, p2
