import re

import networkx

with open('input') as f:
    file = [i.rstrip() for i in f.readlines()]

# Build the graph
graph = networkx.DiGraph()
for line in file:
    foo = re.match(r'(.*) bags contain (.*)$', line)
    color = foo.group(1)
    contains = foo.group(2)
    bags = re.findall(r'([\d]+) (.*?) bag', contains)
    for bag in bags:
        graph.add_edge(color, bag[1], total=int(bag[0]))

# Part 1
print(len(networkx.ancestors(graph, 'shiny gold')))


# Part 2
def recursive_count(bag_choice):
    total_bags = 0
    for k, v in graph[bag_choice].items():
        total_bags += v['total'] * (1 + recursive_count(k))
    return total_bags


print(recursive_count('shiny gold'))
