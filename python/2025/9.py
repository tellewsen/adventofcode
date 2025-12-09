from aoclib.polygon import ispointinside, Pt, Edge, Poly


def solver(myinput: str):
    return p1(myinput), p2(myinput)


def p1(myinput: str):
    #     myinput = """7,1
    # 11,1
    # 11,7
    # 9,7
    # 9,5
    # 2,5
    # 2,3
    # 7,3
    # """
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


# 4755140397 low


def p2(myinput: str):
    coords = []
    for i in myinput.splitlines():
        a, b = i.split(",")
        coords.append(Pt(x=int(a), y=int(b)))
    boundary_set = set(coords)
    edges = []
    for i in range(len(coords) - 1):
        edges.append(Edge(a=coords[i], b=coords[i + 1]))
    edges.append(Edge(a=coords[-1], b=coords[0]))

    poly = Poly(
        name="Remember to plot it to see what it looks like",
        edges=tuple(edges),
    )

    best_coords = None
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
                    best_coords = coords[i], coords[j]
    # high: 4_566_760_900
    # high: 4_664_572_758
    print(best_coords)
    return max_area
