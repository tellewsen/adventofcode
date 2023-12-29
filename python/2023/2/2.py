import re

with open("input") as f:
    lines = f.read().splitlines()
games = {}
for line in lines:
    gid, all_rounds = line.split(":")
    sep = all_rounds.split(";")
    rounds = []
    for gm in sep:
        red = re.search("(\d+) red", gm)
        blue = re.search("(\d+) blue", gm)
        green = re.search("(\d+) green", gm)
        rounds.append(
            (
                int(red.groups()[0]) if red else 0,
                int(green.groups()[0]) if green else 0,
                int(blue.groups()[0]) if blue else 0,
            )
        )
    games[int(gid.split()[1])] = rounds

p1 = 0
p2 = 0
for gid, rounds in games.items():
    possible = True
    mins = [0, 0, 0]
    for round in rounds:
        for i in range(3):
            if round[i] > mins[i]:
                mins[i] = round[i]
        if round[0] > 12 or round[1] > 13 or round[2] > 14:
            possible = False
    p2 += mins[0] * mins[1] * mins[2]

    if possible:
        p1 += gid

print(p1)
print(p2)
