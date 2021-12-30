with open('input') as f:
    file = f.read().rstrip().split('\n\n')

groups = [[set(b) for b in a.split('\n')] for a in file]


def counting_func(groups, set_op):
    sub_counts = []
    for group in groups:
        start = group[0]
        for sub_group in group[1:]:
            start = set_op(start, sub_group)
        sub_counts.append(len(start))
    return sum(sub_counts)


# Part 1
print(counting_func(groups, lambda x, y: x | y))

# Part 2
print(counting_func(groups, lambda x, y: x & y))
