import networkx as nx
import numpy as np


def graph_from_data(data):
    """Create a Graph with directional weights from data"""
    G = nx.DiGraph()
    for x, y in np.ndindex(data.shape):
        if x > 0:
            # from previous to current
            G.add_edge((x - 1, y), (x, y), weight=data[(x, y)])
        if x < data.shape[0]:
            # from next to current
            G.add_edge((x + 1, y), (x, y), weight=data[(x, y)])
        if y > 0:
            # from previous to current
            G.add_edge((x, y - 1), (x, y), weight=data[(x, y)])
        if y < data.shape[1]:
            # from next to current
            G.add_edge((x, y + 1), (x, y), weight=data[(x, y)])
    return G


def p1(data):
    graph = graph_from_data(data)
    stop = (data.shape[0] - 1, data.shape[1] - 1)
    print(1, nx.dijkstra_path_length(graph, (0, 0), stop))


def grow(data):
    data = np.concatenate([data, data + 1, data + 2, data + 3, data + 4], axis=0)
    data = np.concatenate([data, data + 1, data + 2, data + 3, data + 4], axis=1)
    for x, y in np.ndindex(data.shape):
        if data[x, y] > 9:
            data[x, y] -= 9
    return data


def p2(data):
    grown_data = grow(data)
    graph = graph_from_data(grown_data)
    stop = (grown_data.shape[0] - 1, grown_data.shape[1] - 1)
    print(2, nx.dijkstra_path_length(graph, (0, 0), stop))


def main():
    data = np.genfromtxt("input.txt", delimiter=1, dtype=int)
    p1(data)
    p2(data)


if __name__ == "__main__":
    main()
