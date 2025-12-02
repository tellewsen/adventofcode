"""
Started this one out with a dict and recursion but hated it. Checked out reddit
and found everyone were using this awesome package called networkx. So now this
is obviously the way to go. Feels like cheating. I just wanted to see what my
stupid mistake was, not get the solution handed to me with two lines of code.
How have I never heard of this before..
"""

import networkx as nx

data = [line.strip().split(")") for line in open("input", "r").readlines()]
g = nx.Graph(data)
part1 = sum(nx.shortest_path_length(g, x, "COM") for x in g.nodes)
part2 = nx.shortest_path_length(g, "YOU", "SAN") - 2

print(part1)
print(part2)
