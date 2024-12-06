from aoclib import find_word_occurences_in_grid


def solver(text: str):
    # occurrences = find_target_occurrences(text.splitlines())
    return find_word_occurences_in_grid(text.splitlines()), part2(text.splitlines())


def part2(grid: list[str]):
    rows = len(grid)
    cols = len(grid[0])
    count = 0
    for r in range(1, rows - 1):
        for c in range(1, cols - 1):
            if grid[r][c] == "A":
                if (
                    grid[r - 1][c - 1] == "M"
                    and grid[r + 1][c + 1] == "S"
                    or grid[r - 1][c - 1] == "S"
                    and grid[r + 1][c + 1] == "M"
                ) and (
                    grid[r - 1][c + 1] == "M"
                    and grid[r + 1][c - 1] == "S"
                    or grid[r - 1][c + 1] == "S"
                    and grid[r + 1][c - 1] == "M"
                ):
                    count += 1
    return count


def find_target_occurrences(grid: list[str], target="XMAS"):
    """
    TODO: Figure out why this misses some
    """
    rows = len(grid)
    cols = len(grid[0])
    target_len = len(target)
    count = 0
    for r in range(rows):
        for c in range(cols):
            is_inside_right = c + target_len <= cols
            is_inside_left = c - target_len + 1 >= 0
            is_inside_down = r + target_len <= rows
            is_inside_up = r - target_len + 1 >= 0
            # Horizontal right
            if is_inside_right and grid[r][c : c + target_len] == target:
                count += 1

            # Horizontal left
            if is_inside_left and grid[r][c : c - target_len : -1] == target:
                count += 1

            # Vertical down
            if (
                is_inside_down
                and "".join(grid[r + i][c] for i in range(target_len)) == target
            ):
                count += 1

            # Vertical up
            if (
                is_inside_up
                and "".join(grid[r - i][c] for i in range(target_len)) == target
            ):
                count += 1

            # Diagonal bottom-right
            if (
                is_inside_down
                and is_inside_right
                and "".join(grid[r + i][c + i] for i in range(target_len)) == target
            ):
                count += 1

            # Diagonal bottom-left
            if (
                is_inside_down
                and is_inside_left
                and "".join(grid[r + i][c - i] for i in range(target_len)) == target
            ):
                count += 1

            # Diagonal top-right
            if (
                is_inside_up
                and is_inside_right
                and "".join(grid[r - i][c + i] for i in range(target_len)) == target
            ):
                count += 1

            # Diagonal top-left
            if (
                is_inside_up
                and is_inside_left
                and "".join(grid[r - i][c - i] for i in range(target_len)) == target
            ):
                count += 1
    return count
