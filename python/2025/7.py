import numpy as np
from functools import cache


def solver(myinput: str):
    return both(myinput)


def make_grid(myinput: str):
    lines = myinput.splitlines()
    grid = np.zeros((len(lines), len(lines[0])), dtype=int)
    for r, line in enumerate(lines):
        for c, ch in enumerate(line):
            if ch == "^":
                grid[r, c] = 1
            if ch == "S":
                grid[r, c] = 2
    return grid


def both(myinput: str):
    grid = make_grid(myinput)
    splits = 0

    for i, row in enumerate(grid):
        for j, val in enumerate(row):
            if val == 2:  # start
                grid[i + 1, j] = 3
            if val == 1 and grid[i - 1, j] == 3:  # split
                splits += 1
                grid[i + 1, j + 1] = 3
                grid[i + 1, j - 1] = 3
            if val == 3 and i < len(grid) - 1:  # keep going
                if grid[i + 1, j] == 0:
                    grid[i + 1, j] = 3

    @cache
    def walk(x, y):
        if x >= len(grid):
            return 1
        if y < 0 or y >= len(grid[0]):
            return 0
        if grid[x, y] == 1:
            return walk(x + 1, y - 1) + walk(x + 1, y + 1)
        if grid[x, y] == 2:
            return walk(x + 1, y)
        if grid[x, y] == 3:
            return walk(x + 1, y)
        return 0

    return splits, walk(0, np.where(grid[0] == 2)[0][0])
