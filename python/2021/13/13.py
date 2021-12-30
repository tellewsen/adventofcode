import numpy as np


def read_file(filename):
    marks = set()
    folds = []
    with open(filename, "r") as f:
        for line in f.readlines():
            line = line.rstrip()
            if line.startswith("fold"):
                coors, val = line.split(" ")[-1].split("=")
                folds.append((coors, int(val)))
            elif line == "":
                continue
            else:
                x, y = line.split(",")
                marks.add((int(x), int(y)))
    return marks, folds


def fold_once(marks, fold):
    new_marks = set()
    coord, fold_val = fold

    for x, y in marks:
        # flipping along x or y ?
        cond_val = x if coord == "x" else y
        # non flip side
        if cond_val < fold_val:
            new_marks.add((x, y))
            continue
        # flip side
        if coord == "x":
            new = (fold_val - (x - fold_val), y)
        else:
            new = (x, fold_val - (y - fold_val))
        new_marks.add(new)
    return new_marks


def fold(marks, folds, p1):
    for fold_intruction in folds:
        marks = fold_once(marks, fold_intruction)
        if p1:
            break
    return marks


def p1(marks, folds):
    return len(fold(marks, folds, True))


def p2(marks, folds):
    marks = fold(marks, folds, False)
    # mark chars on a grid
    max_x = max([i[0] for i in marks])
    max_y = max([i[1] for i in marks])
    grid = np.zeros((max_x + 1, max_y + 1))
    for mark in marks:
        grid[mark] = 1
    # Output result
    for line in np.rot90(np.transpose(np.rot90(grid, 1))):
        print("".join([i and "#" or "." for i in line]))


def main():
    marks, folds = read_file("input.txt")
    print(1, p1(marks, folds))
    marks, folds = read_file("input.txt")
    p2(marks, folds)


if __name__ == "__main__":
    main()
