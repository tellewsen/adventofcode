def solver(text):
    grid = text.splitlines()
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # up, right, down, left
    dir_idx = 0
    for i in range(len(grid)):
        if "^" in grid[i]:
            pos = (i, grid[i].index("^"))
            break
    rows = len(grid)
    cols = len(grid[0])
    visited = set()
    visited.add(pos)
    while True:
        next_pos = (pos[0] + dirs[dir_idx][0], pos[1] + dirs[dir_idx][1])
        if not (0 <= next_pos[0] < rows) or not (0 <= next_pos[1] < cols):
            break
        if grid[next_pos[0]][next_pos[1]] == "#":
            dir_idx = (dir_idx + 1) % 4
        else:
            pos = next_pos
            visited.add(pos)
    return len(visited), 1
