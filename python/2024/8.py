from collections import defaultdict
from itertools import combinations


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
    for k, vs in antennas.items():
        combos = combinations(vs, 2)
        for s in combos:
            a, b = s
            xdiff = b[0] - a[0]
            ydiff = b[1] - a[1]
            c1 = (a[0] - xdiff, a[1] - ydiff)
            c2 = (b[0] + xdiff, b[1] + ydiff)
            print(vs, s, xdiff, ydiff, c1, c2)
            if 0 <= c1[0] < rows and 0 <= c1[1] < cols:
                antinodes.add(c1)
            if 0 <= c2[0] < rows and 0 <= c2[1] < cols:
                antinodes.add(c2)
    return len(antinodes), 1
