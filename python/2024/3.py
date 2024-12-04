# Regex
import re

def solver(lines):
    matches = re.findall(r"mul\(\d+,\d+\)", lines)
    r = 0
    for m in matches:
        g = m.split(",")
        res = int(g[0][4:]) * int(g[1][:-1])
        r += res
    return r
