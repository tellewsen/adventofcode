from collections import defaultdict
from itertools import combinations, product
import math


def solver(text):
    data = text.splitlines()
    rows = len(data)
    cols = len(data[0])
    antennas = defaultdict(list)
    for r in range(rows):
        for c in range(cols):
            if data[r][c] != ".":
                antennas[data[r][c]].append((r, c))
    antinodes = set()
    extras = set()
    for k, vs in antennas.items():
        combos = combinations(vs, 2)
        for a, b in combos:
            dx = b[0] - a[0]
            dy = b[1] - a[1]
            # part 1
            c1 = (a[0] - dx, a[1] - dy)
            if 0 <= c1[0] < cols and 0 <= c1[1] < rows:
                antinodes.add(c1)
            c2 = (b[0] + dx, b[1] + dy)
            if 0 <= c2[0] < cols and 0 <= c2[1] < rows:
                antinodes.add(c2)
            # Part 2
            gcd = math.gcd(dx, dy)
            dx = dx / gcd
            dy = dy / gcd
            c1 = (a[0] - dx, a[1] - dy)
            c2 = (a[0] + dx, a[1] + dy)
            while 0 <= c1[0] < cols and 0 <= c1[1] < rows:
                extras.add(c1)
                c1 = (c1[0] - dx, c1[1] - dy)
            while 0 <= c2[0] < cols and 0 <= c2[1] < rows:
                extras.add(c2)
                c2 = (c2[0] + dx, c2[1] + dy)
            extras.add(a)
            extras.add(b)
    return len(antinodes), len(extras)


# 931 low
# 951 low
# 1009 low
