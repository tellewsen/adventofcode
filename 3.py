# Regex
import re

with open("input") as f:
    lines = f.read()


matches = re.findall(r"mul\(\d+,\d+\)", lines)
print(matches)

r = 0
for m in matches:
    g = m.split(",")
    res = int(g[0][4:]) * int(g[1][:-1])
    r += res
print(r)
