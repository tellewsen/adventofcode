with open('input') as f:
    file = f.read().splitlines()


def evolve_grid(part, grid):
    rule = {1: 4, 2: 5}
    return_grid = []
    for i in range(len(grid)):
        row = ''
        for j in range(len(grid[0])):
            adjacent = ''
            for m in (-1, 0, 1):
                for n in (-1, 0, 1):
                    if m == n == 0:
                        continue
                    if part == 1:
                        if 0 <= i+m < len(grid) and 0 <= j+n < len(grid[0]):
                            adjacent += grid[i+m][j+n]
                    elif part == 2:
                        step = 1
                        while (
                                0 <= i+step*m < len(grid)
                                and 0 <= j+step*n < len(grid[0])
                        ):
                            view = grid[i+step*m][j+step*n]
                            if view in ('#', 'L'):
                                adjacent += view
                                break
                            step += 1
                    else:
                        print('bad part')
                        import sys; sys.exit()
            if grid[i][j] == '#' and adjacent.count('#') >= rule[part]:
                row += 'L'
            elif grid[i][j] == 'L' and adjacent.count('#') == 0:
                row += '#'
            else:
                row += grid[i][j]
        return_grid.append(row)
    return return_grid


# Part 1
def get_answer(part, grid):
    while True:
        next_grid = evolve_grid(part, grid)
        if next_grid == grid:
            count = [i.count('#') for i in grid]
            break
        grid = next_grid
    return sum(count)


print(get_answer(1, file))
print(get_answer(2, file))
