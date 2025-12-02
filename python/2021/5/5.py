import numpy as np


def read_file(filename):
    with open(filename, "r") as f:
        data = [i.rstrip() for i in f.readlines()]
    return data


def mark_points(grid, start, end, skip_diagonal):
    x, y = start
    x_e, y_e = end
    dx = -1 if x > x_e else 1 if x < x_e else 0
    dy = -1 if y > y_e else 1 if y < y_e else 0
    if skip_diagonal:
        if dx != 0 and dy != 0:
            return
    grid[x, y] += 1
    while (x, y) != end:
        x += dx
        y += dy
        grid[x, y] += 1


def parse_content(content, skip_diagonal):
    grid = np.zeros((1000, 1000), dtype=int)
    for line in content:
        start, stop = line.split(" -> ")
        x1, y1 = start.split(",")
        x2, y2 = stop.split(",")
        start = int(x1), int(y1)
        end = int(x2), int(y2)
        mark_points(grid, start, end, skip_diagonal)
    return grid


def p1(content):
    parsed = parse_content(content, skip_diagonal=True)
    return (parsed > 1).sum()


def p2(content):
    parsed = parse_content(content, skip_diagonal=False)
    return (parsed > 1).sum()


def main():
    content = read_file("input.txt")
    print(1, p1(content))
    print(2, p2(content))


if __name__ == "__main__":
    main()
