import numpy as np


def read_file(filename):
    with open(filename, "r") as f:
        data = [i.rstrip() for i in f.readlines()]
    grid = np.empty((10, 10), dtype=int)
    for i, line in enumerate(data):
        for j, char in enumerate(line):
            grid[i, j] = char
    return grid


def get_neighbours(hm, x, y):
    neighbours = []
    max_x = len(hm) - 1
    max_y = len(hm[0]) - 1
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            if 0 <= x+i <= max_x and 0 <= y+j <= max_y:
                neighbours.append((x+i, y+j))
    return neighbours


def evolve(grid):
    flashes = np.zeros((10, 10), dtype=bool)

    # increase all by one
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            grid[i, j] += 1
    keep_going = True
    while keep_going:
        keep_going = False
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x, y] > 9:
                    keep_going = True
                    flashes[x, y] = True
                    grid[x, y] = 0
                    neighbours = get_neighbours(grid, x, y)
                    for neigh in neighbours:
                        if flashes[neigh]:  # skip already flashed
                            continue
                        grid[neigh] += 1

    return np.count_nonzero(flashes)


def p1(grid):
    flashcounter = 0
    for _ in range(100):
        flashcounter += evolve(grid)
    return flashcounter


def p2(grid):
    for x in range(1000):
        evolve(grid)
        if np.count_nonzero(grid) == 0:
            return x+1


def main():
    print(1, p1(read_file("input.txt")))
    print(2, p2(read_file("input.txt")))


if __name__ == "__main__":
    main()
