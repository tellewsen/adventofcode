from collections import defaultdict


def read_file(filename):
    with open(filename, "r") as f:
        data = [tuple(i.rstrip().split("-")) for i in f.readlines()]
    return data


def data2connections(data):
    """
    Create a defaultdict with all paths to other nodes for each node

    Multiple can point to end, but end points nowhere.
    """
    connections = defaultdict(list)
    for pair in data:
        for p1, p2 in zip(pair, reversed(pair)):
            if p2 != "start":
                connections[p1].append(p2)
    del connections["end"]
    return connections


def p1(connections, path):
    """
    Walk the path recursively until we find the end

    Stops when we reach a node with no connections, in this case the
    "end" node we removed when parsing data.
    """
    num_paths = 0
    for point in connections[path[-1]]:
        if point not in path or point.isupper():
            if point == "end":
                # found the end
                num_paths += 1
            else:
                # keep going
                num_paths += p1(connections, path + [point])
    return num_paths


def p2(connections, path):
    """Same as p1 with the extra small cave stop allowed"""
    num_paths = 0
    for point in connections[path[-1]]:
        if point == "end":
            # found the end
            num_paths += 1
        else:
            # keep going
            if point in path and point.islower():
                # Use the extra trip through a small cave
                num_paths += p1(connections, path + [point])
            else:
                # still going with possible extra trip
                num_paths += p2(connections, path + [point])
    return num_paths


def main():
    data = data2connections(read_file("input.txt"))
    print(1, p1(data, ["start"]))
    print(2, p2(data, ["start"]))


if __name__ == "__main__":
    main()
