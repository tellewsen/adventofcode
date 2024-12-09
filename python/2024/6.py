from collections import defaultdict


def walk_guard(grid: list[str], pos, dir_idx):
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # up, right, down, left
    visited = defaultdict(int)
    visited[pos] += 1
    rows = len(grid)
    cols = len(grid[0])
    while True:
        if visited[pos] > 4:
            return visited, True
        next_pos = (pos[0] + dirs[dir_idx][0], pos[1] + dirs[dir_idx][1])
        if not (0 <= next_pos[0] < rows) or not (0 <= next_pos[1] < cols):
            break
        if grid[next_pos[0]][next_pos[1]] == "#":
            dir_idx = (dir_idx + 1) % 4
        else:
            pos = next_pos
            visited[pos] += 1
    return visited, False


def solver(text):
    grid = text.splitlines()
    dir_idx = 0
    for i in range(len(grid)):
        if "^" in grid[i]:
            pos = (i, grid[i].index("^"))
            break
    p1, _ = walk_guard(grid, pos, dir_idx)
    # We're only looking at the path the guard alrady walks since
    # placing obstacles any other place won't matter
    candidates = p1.keys()
    loops = 0
    for c in candidates:
        grid_copy = grid.copy()
        row_copy = grid_copy[c[0]]
        grid_copy[c[0]] = "".join([row_copy[: c[1]], "#", row_copy[c[1] + 1 :]])
        _, looped = walk_guard(grid_copy, pos, dir_idx)
        loops += int(looped)
    return len(p1), loops
