foo = []
with open('input') as f:
    file = f.read().splitlines()
    for i in file:
        bar = i.split(' ')
        minimum, maximum = bar[0].split('-')
        char = bar[1][0]
        password = bar[2]
        foo.append((int(minimum), int(maximum), char, password))

# part 1
score = 0
for stuff in foo:
    if stuff[0] <= stuff[3].count(stuff[2]) <= stuff[1]:
        score += 1
print(score)

# part 2
score = 0
for stuff in foo:
    if stuff[3][stuff[0]-1] == stuff[2] and stuff[3][stuff[1]-1] == stuff[2]:
        continue
    if stuff[3][stuff[0]-1] == stuff[2] or stuff[3][stuff[1]-1] == stuff[2]:
        score += 1
print(score)
