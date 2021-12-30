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


def get_neighbours(hm, x, y):
    neighbours = []
    max_x = len(hm) - 1
    max_y = len(hm[0]) - 1
    if y == 0:
        neighbours.append((x, y + 1))
    elif y == max_y:
        neighbours.append((x, y - 1))
    else:
        neighbours.append((x, y + 1))
        neighbours.append((x, y - 1))
    if x == 0:
        neighbours.append((x + 1, y))
    elif x == max_x:
        neighbours.append((x - 1, y))
    else:
        neighbours.append((x + 1, y))
        neighbours.append((x - 1, y))
    return neighbours


def is_lowpoint(hm, x, y):
    neighbours = get_neighbours(hm, x, y)
    for neigh in neighbours:
        if hm[x, y] >= hm[neigh[0], neigh[1]]:
            return False
    return True


def fetch_lowpoints(hm):
    lowpoints = []
    for i, row in enumerate(hm):
        for j, _ in enumerate(row):
            if is_lowpoint(hm, i, j):
                lowpoints.append((i, j))
    return lowpoints


def p1(hm):
    lowpoints = fetch_lowpoints(hm)
    return sum(i + 1 for i in [hm[point] for point in lowpoints])


def gather_basin_members(hm, basin, x, y):
    neighbours = get_neighbours(hm, x, y)
    if hm[x, y] != 9 and (x, y) not in basin:
        basin.add((x, y))
    for neigh in neighbours:
        if neigh in basin:
            continue
        if hm[neigh] == 9:
            continue
        else:
            basin.add((x, y))
            gather_basin_members(hm, basin, neigh[0], neigh[1])


def p2(hm):
    lowpoints = fetch_lowpoints(hm)
    basins = [{i} for i in lowpoints]
    for basin in basins:
        x, y = next(iter(basin))
        gather_basin_members(hm, basin, x, y)
    lengths = [len(i) for i in basins]
    length_sorted_basins = sorted(zip(lengths, basins), reverse=True)[:3]
    return np.prod([i[0] for i in length_sorted_basins])


def main():
    filename = "input.txt"
    hm = read_file(filename)
    print(1, p1(hm))
    print(2, p2(hm))


if __name__ == "__main__":
    main()
