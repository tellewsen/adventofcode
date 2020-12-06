with open('input') as f:
    file = f.read().rstrip().split('\n\n')

# Part 1
groups = [a.replace('\n', '') for a in file]
b = [set() for _ in groups]
for i in range(len(groups)):
    for j in groups[i]:
        b[i].add(j)
print(sum([len(i) for i in b]))

# Part 2
part2 = [a.split('\n') for a in file]


def char_in_rest(char, rest):
    in_all = True
    for entry in rest:
        if char not in entry:
            in_all = False
            break
    return in_all


in_rest = []
for group in part2:
    for character in group[0]:
        in_rest.append(char_in_rest(character, group[0:]))
print(sum(in_rest))
