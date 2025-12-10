from aoclib.polygon import ispointinside, Pt, Edge, Poly


def solver(myinput: str):
    return p1(myinput), p2(myinput)


def p1(myinput: str):
    coords = []
    for i in myinput.splitlines():
        a, b = i.split(",")
        coords.append((int(a), int(b)))
    max_area = 0
    for i in range(len(coords)):
        for j in range(i + 1, len(coords)):
            x1, y1 = coords[i]
            x2, y2 = coords[j]
            area = (abs((x2 - x1)) + 1) * (abs(y2 - y1) + 1)

            if area > max_area:
                max_area = area

    return max_area


def p2(myinput: str):
    """TODO: This does not work.

    I tried a bunch of stuff from other people and it worked at some point
    but then I changed something and it broke and now I can't figure out
    what. I think computing the sizes beforehand, sorting them and the edges
    and then working through in descending order did the trick.

    For the record I hate this problem.
    """
    coords = [
        Pt(x=int(a), y=int(b))
        for a, b in (line.split(",") for line in myinput.splitlines())
    ]
    boundary_set = set(coords)
    edges = []
    for i in range(len(coords) - 1):
        edges.append(Edge(a=coords[i], b=coords[i + 1]))
    edges.append(Edge(a=coords[-1], b=coords[0]))

    poly = Poly(
        name="Remember to plot it to see what it looks like",
        edges=tuple(edges),
    )
    max_area = 0
    for i in range(len(coords)):
        for j in range(i + 1, len(coords)):
            x1, y1 = coords[i]
            x2, y2 = coords[j]

            min_x, max_x = min(x1, x2), max(x1, x2)
            min_y, max_y = min(y1, y2), max(y1, y2)
            corners = [
                Pt(x=min_x, y=min_y),
                Pt(x=max_x, y=min_y),
                Pt(x=max_x, y=max_y),
                Pt(x=min_x, y=max_y),
            ]
            if all(
                (corner in boundary_set or ispointinside(corner, poly))
                for corner in corners
            ):
                area = (abs((x2 - x1)) + 1) * (abs(y2 - y1) + 1)
                # print(x1, y1, x2, y2, area)
                if area > max_area:
                    max_area = area
    return max_area
