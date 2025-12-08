import math

Coord = tuple[int, int, int]


class UnionFind:
    """Helper class for making connections


    Kruskal's Algorithm: https://en.wikipedia.org/wiki/Kruskal%27s_algorithm"""

    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
        self.num_components = n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y: int):
        root_x, root_y = self.find(x), self.find(y)
        if root_x == root_y:
            return False  # Already connected
        if self.size[root_x] < self.size[root_y]:
            root_x, root_y = root_y, root_x
        self.parent[root_y] = root_x
        self.size[root_x] += self.size[root_y]
        self.num_components -= 1
        return True


def solver(myinput: str):
    return p1(myinput), p2(myinput)


def p1(myinput: str):
    nodes = [tuple(map(int, line.split(","))) for line in myinput.splitlines()]
    # Make list with distances and coords sorted by increasing distance
    edges = []
    for i in range(len(nodes)):
        for j in range(i + 1, len(nodes)):
            dist = distance(nodes[i], nodes[j])
            edges.append((dist, i, j))
    edges.sort()

    # Make 1k attempts at connecting
    uf = UnionFind(len(nodes))
    attempts = 0
    for dist, i, j in edges:
        attempts += 1
        uf.union(i, j)
        if attempts == 1000:
            break

    # Count circuit sizes
    circuit_sizes = {}
    for i in range(len(nodes)):
        root = uf.find(i)
        circuit_sizes[root] = circuit_sizes.get(root, 0) + 1

    # Get the three largest circuits
    sizes = sorted(circuit_sizes.values(), reverse=True)
    result = sizes[0] * sizes[1] * sizes[2]
    return result


def p2(myinput: str):
    nodes = [tuple(map(int, line.split(","))) for line in myinput.splitlines()]
    # Make list with distances and coords sorted by increasing distance
    edges = []
    for i in range(len(nodes)):
        for j in range(i + 1, len(nodes)):
            dist = distance(nodes[i], nodes[j])
            edges.append((dist, i, j))
    edges.sort()

    # Connect until all boxes are in one circuit
    uf = UnionFind(len(nodes))

    for dist, i, j in edges:
        if uf.union(i, j):
            # Check if all boxes are now in one circuit
            if uf.num_components == 1:
                return nodes[i][0] * nodes[j][0]
    raise ValueError("Something wrong")


def distance(a: Coord, b: Coord) -> float:
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2 + (a[2] - b[2]) ** 2)
