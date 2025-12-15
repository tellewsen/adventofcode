def solver(myinp: str):
    p1(myinp)


def parse_input(myinp: str):
    """Parse shapes and regions from input."""
    lines = myinp.strip().split("\n")

    shapes = {}
    regions = []

    i = 0
    # Parse shapes - look for lines ending with ':'
    while i < len(lines):
        line = lines[i].strip()
        if not line:
            i += 1
            continue
        # Check if this is a shape definition (number followed by colon)
        if line.endswith(":") and line[:-1].isdigit():
            shape_idx = int(line[:-1])
            shape_lines = []
            i += 1
            # Read shape lines until we hit another shape definition or region
            while i < len(lines):
                line = lines[i].strip()
                if not line:
                    i += 1
                    break
                # Check if next shape or region
                if line.endswith(":") and line[:-1].isdigit():
                    break
                if "x" in line and ":" in line:
                    break
                shape_lines.append(line)
                i += 1
            shapes[shape_idx] = shape_lines
        # Check if this is a region definition (contains 'x' and ':')
        elif "x" in line and ":" in line:
            parts = line.split()
            dims = parts[0].rstrip(":").split("x")
            width, height = int(dims[0]), int(dims[1])
            counts = [int(x) for x in parts[1:]]
            regions.append((width, height, counts))
            i += 1
        else:
            i += 1

    return shapes, regions


def get_shape_coords(shape_lines):
    """Extract coordinates of '#' cells from shape."""
    coords = []
    for r, line in enumerate(shape_lines):
        for c, ch in enumerate(line):
            if ch == "#":
                coords.append((r, c))
    return coords


def normalize_coords(coords):
    """Normalize coordinates to start at (0, 0)."""
    if not coords:
        return []
    min_r = min(r for r, c in coords)
    min_c = min(c for r, c in coords)
    return sorted([(r - min_r, c - min_c) for r, c in coords])


def rotate_coords(coords):
    """Rotate coordinates 90 degrees clockwise."""
    # (r, c) -> (c, -r) but we normalize after
    return [(c, -r) for r, c in coords]


def flip_coords(coords):
    """Flip coordinates horizontally."""
    return [(r, -c) for r, c in coords]


def get_all_orientations(shape_lines):
    """Generate all unique orientations (rotations and flips) of a shape."""
    coords = get_shape_coords(shape_lines)
    orientations = set()

    # Try all combinations of rotations and flips
    current = coords
    for _ in range(4):  # 4 rotations
        orientations.add(tuple(normalize_coords(current)))
        orientations.add(tuple(normalize_coords(flip_coords(current))))
        current = rotate_coords(current)

    return [list(o) for o in orientations]


def can_place(grid, coords, row, col):
    """Check if shape can be placed at (row, col)."""
    for dr, dc in coords:
        r, c = row + dr, col + dc
        if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]):
            return False
        if grid[r][c]:
            return False
    return True


def place_shape(grid, coords, row, col, value):
    """Place or remove shape from grid."""
    for dr, dc in coords:
        r, c = row + dr, col + dc
        if 0 <= r < len(grid) and 0 <= c < len(grid[0]):
            grid[r][c] = value


def solve_region(width, height, shapes_dict, counts):
    """Try to fit all required presents into the region."""

    # Create grid
    grid = [[0] * width for _ in range(height)]

    # Build list of presents to place
    presents = []
    for shape_idx, count in enumerate(counts):
        for _ in range(count):
            presents.append(shape_idx)

    # Check if total area fits
    total_area = sum(len(get_shape_coords(shapes_dict[idx])) for idx in presents)
    if total_area > width * height:
        return False

    # Precompute all orientations for each shape
    shape_orientations = {}
    for idx in shapes_dict:
        shape_orientations[idx] = get_all_orientations(shapes_dict[idx])

    def backtrack(present_idx):
        """Recursively try to place all presents."""

        if present_idx >= len(presents):
            return True

        shape_idx = presents[present_idx]

        # Try each orientation of this shape
        for orientation in shape_orientations[shape_idx]:
            # Try each position in the grid
            for row in range(height):
                for col in range(width):
                    if can_place(grid, orientation, row, col):
                        # Place the shape
                        place_shape(grid, orientation, row, col, present_idx + 1)

                        # Recurse
                        result = backtrack(present_idx + 1)
                        if result is None:
                            return None
                        if result:
                            return True

                        # Backtrack
                        place_shape(grid, orientation, row, col, 0)

        return False

    result = backtrack(0)
    return False if result is None else result


def p1(myinp: str):
    print("Parsing regions and shapes...")
    shapes, regions = parse_input(myinp)

    count = 0
    print(f"Number of regions: {len(regions)}")
    i = 0
    for width, height, counts in regions:
        print(f"Solving region {i + 1}/{len(regions)}")
        i += 1

        result = solve_region(width, height, shapes, counts)
        if result:
            count += 1

    print(f"Part 1: {count}")


if __name__ == "__main__":
    inp = """0:
###
##.
##.

1:
###
##.
.##

2:
.##
###
##.

3:
##.
###
##.

4:
###
#..
###

5:
###
.#.
###

4x4: 0 0 0 0 2 0
12x5: 1 0 1 0 2 2
12x5: 1 0 1 0 3 2
"""
    solver(inp)
