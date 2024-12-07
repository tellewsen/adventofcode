def solver(text):
    visitmark = "*"
    grid = text.splitlines()
    dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]  # up, right, down, left
    dir_idx = 0
    for i in range(len(grid)):
        if "^" in grid[i]:
            pos = [i, grid[i].index("^")]
            break

    grid[pos[0]] = grid[pos[0]][: pos[1]] + visitmark + grid[pos[0]][pos[1] + 1 :]
    while True:
        print(pos)
        try:
            if grid[pos[0]][pos[1]] == "#":
                dir_idx += 1
                dir_idx = dir_idx % 3
                print(dir_idx)
                continue
        except IndexError:
            break
        pos[0] += dirs[dir_idx][0]
        pos[1] += dirs[dir_idx][1]
        try:
            grid[pos[0]] = (
                grid[pos[0]][: pos[1]] + visitmark + grid[pos[0]][pos[1] + 1 :]
            )
        except IndexError:
            break
    return sum(i.count(visitmark) for i in grid), 1
