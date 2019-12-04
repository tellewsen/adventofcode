"""
Pretty much a copy of a solution I found on reddit after messing around with
grids and realizing there was no point in keeping track of a ton of unused
coordinates.

The hard part of this one is figuring out how to save which coordinates the
wires occupy. The rest is simple arithmetic

Solves it by marking the coordinates of each point of each wire, and then
looking up which points are present in both wires. After that it's straight
forward to find which one is closest to the start.

Expanding it to find the point with the shortest total wire length is simply
done by keeping track of how far each wire has gone and saving that for each
point. Thus to find the point with the shortest length we simply sum the length
of the cables for each intersection point, and pick the minimal one.

"""

# Read data from file
line1, line2, _ = open('input').read().split('\n')
line1, line2 = [i.split(',') for i in (line1, line2)]


# Make the paths
def get_coords(line):
    xmoves = {'R': 1, 'L': -1, 'U': 0, 'D': 0}
    ymoves = {'R': 0, 'L': 0, 'U': 1, 'D': -1}

    x = 0
    y = 0
    coords = {}
    length = 0
    for step in line:
        direction = step[0]
        n_steps = int(step[1:])
        for _ in range(n_steps):
            x += xmoves[direction]
            y += ymoves[direction]
            length += 1
            if (x, y) not in coords:
                coords[(x, y)] = length
    return coords


w1_points = get_coords(line1)
w2_points = get_coords(line2)
in_both = w1_points.keys() & w2_points.keys()
part1 = min(abs(x) + abs(y) for (x, y) in in_both)
part2 = min(w1_points[(x, y)] + w2_points[(x, y)] for (x, y) in in_both)
print(part1)
print(part2)
