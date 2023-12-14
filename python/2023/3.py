import re

with open("input") as f:
    lines = f.read().splitlines()

## PART 1 ##
# Make a structure to work with
partnos = []
for i, line in enumerate(lines):
    matches = re.finditer("\d+", line)
    for j in matches:
        partnos.append((i, j.start(), j.end(), int(j.group())))

# count
partnosum = 0
for pn in partnos:
    adjacentchars = ""
    line_idx = pn[0]
    # above
    if line_idx > 0:
        if pn[1] > 0:
            adjacentchars += lines[line_idx - 1][pn[1] - 1]
        adjacentchars += lines[line_idx - 1][pn[1] : pn[2] + 1]
        if pn[2] < len(lines[line_idx - 1]) - 1:
            adjacentchars += lines[line_idx - 1][pn[2]]

    # left
    if pn[1] > 0:
        adjacentchars += lines[line_idx][pn[1] - 1]
    # right
    if pn[2] < len(lines[line_idx]) - 1:
        right_chars = lines[line_idx][pn[2]]
        adjacentchars += right_chars
    # below
    if line_idx < len(lines[line_idx]) - 1:
        if pn[1] > 0:
            adjacentchars += lines[line_idx + 1][pn[1] - 1]
        adjacentchars += lines[line_idx + 1][pn[1] : pn[2] + 1]
        if pn[2] < len(lines[line_idx + 1]) - 1:
            adjacentchars += lines[line_idx + 1][pn[2]]
    if not re.findall("^[\.]+$", adjacentchars):
        partnosum += pn[3]
    print(pn[3], adjacentchars, partnosum)
    # input()
