def count_neighbors(x: int, y: int, grid: list[list[str]], char="@"):
    count = 0
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dy == dx == 0:
                continue
            if x + dx >= len(grid) or x + dx < 0:
                continue
            if y + dy >= len(grid[0]) or y + dy < 0:
                continue
            if grid[x + dx][y + dy] == char:
                count += 1
    return count


def p1(myinput: str):
    accessible = 0
    grid = myinput.split("\n")
    grid = [[i for i in j] for j in grid]

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "@" and count_neighbors(i, j, grid, "@") < 4:
                accessible += 1

    return accessible


def p2(myinput: str):
    grid = myinput.split("\n")
    grid = [[i for i in j] for j in grid]

    def solve():
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "@" and count_neighbors(i, j, grid, "@") < 4:
                    count += 1
                    grid[i][j] = "."
        return count

    accessible = 0
    while True:
        count = solve()
        accessible += count
        if count == 0:
            break
    return accessible


def solver(myinput: str):
    return p1(myinput), p2(myinput)
