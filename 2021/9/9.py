import numpy as np


def read_file(filename):
    with open(filename, "r") as f:
        data = [i.rstrip() for i in f.readlines()]
    x = len(data)
    y = len(data[0])
    grid = np.zeros((x, y), dtype=int)
    for i in range(x):
        for j in range(y):
            grid[i, j] = data[i][j]
    return grid


def is_lowpoint(hm, x, y):
    neighbours = []
    max_x = len(hm) - 1
    max_y = len(hm[0]) - 1
    if y == 0:
        neighbours.append(hm[x, y + 1])
    elif y == max_y:
        neighbours.append(hm[x, y - 1])
    else:
        neighbours.append(hm[x, y + 1])
        neighbours.append(hm[x, y - 1])
    if x == 0:
        neighbours.append(hm[x + 1, y])
    elif x == max_x:
        neighbours.append(hm[x - 1, y])
    else:
        neighbours.append(hm[x + 1, y])
        neighbours.append(hm[x - 1, y])
    for neigh in neighbours:
        if hm[x, y] >= neigh:
            return False
    return True


def p1(hm):
    lowpoints = []
    for i, row in enumerate(hm):
        for j, _ in enumerate(row):
            if is_lowpoint(hm, i, j):
                lowpoints.append(hm[i, j])
    print(lowpoints)
    return sum(i + 1 for i in lowpoints)


def p2(content):
    ...


def main():
    filename = "input.txt"
    # filename = "example_input.txt"
    hm = read_file(filename)
    print(1, p1(hm))
    print(2, p2(hm))


if __name__ == "__main__":
    main()
