import math
from itertools import combinations

import networkx as nx

Coord = tuple[int, int, int]


def solver(myinput: str):
    return p1(myinput), p2(myinput)


def p1(myinput: str):
    nodes = [tuple(map(int, line.split(","))) for line in myinput.splitlines()]
    edges = sorted(
        (distance(nodes[i], nodes[j]), i, j)
        for i, j in combinations(range(len(nodes)), 2)
    )

    G = nx.Graph()
    G.add_edges_from((i, j) for _, i, j in edges[:1000])

    sizes = sorted((len(c) for c in nx.connected_components(G)), reverse=True)
    return math.prod(sizes[:3])


def p2(myinput: str):
    nodes = [tuple(map(int, line.split(","))) for line in myinput.splitlines()]
    edges = sorted(
        (distance(nodes[i], nodes[j]), i, j)
        for i, j in combinations(range(len(nodes)), 2)
    )

    G = nx.Graph()
    for _, i, j in edges:
        G.add_edge(i, j)
        if nx.is_connected(G):
            return nodes[i][0] * nodes[j][0]


def distance(a: Coord, b: Coord) -> float:
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2 + (a[2] - b[2]) ** 2)
