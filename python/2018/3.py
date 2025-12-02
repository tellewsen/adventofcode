from collections import defaultdict

with open("3.txt") as f:
    puz = f.read().splitlines()

# p1:
claims = {}
claim_ids = set()
for line in puz:
    num, _, coords, size = line.split(" ")
    num = num[1:]
    claim_ids.add(num)
    xw, yw = size.split("x")
    xw = int(xw)
    yw = int(yw)
    xcord, ycord = coords.rstrip(":").split(",")
    xcord = int(xcord)
    ycord = int(ycord)
    for x in range(xw):
        for y in range(yw):
            if (xcord + x, ycord + y) not in claims:
                claims[(xcord + x, ycord + y)] = [num]
            else:
                claims[(xcord + x, ycord + y)].append(num)
overlaps = 0

for k, v in claims.items():
    if len(v) > 1:
        overlaps += 1
        for i in v:
            try:
                claim_ids.remove(i)
            except KeyError:
                pass


print(1, overlaps)
print(2, claim_ids)
