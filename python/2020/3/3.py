import numpy

with open("input") as f:
    file = f.read().splitlines()
bar = []
for i in file:
    bar.append(i.replace(".", "0").replace("#", "1"))
xlen = len(bar[0])
ylen = len(bar)
grid = numpy.zeros((ylen, xlen))
for i in range(0, xlen):
    for j in range(0, ylen):
        temp = int(bar[j][i])
        grid[j][i] = temp


def slope_check(xstep, ystep):
    x = 0
    y = 0
    count = 0
    while y <= 322:
        if x > xlen - xstep:
            x -= xlen
        if grid[y][x]:
            count += 1
        x += xstep
        y += ystep
    return count


# Part 1
print(slope_check(3, 1))

# Part 2
slopes = (1, 1), (3, 1), (5, 1), (7, 1), (1, 2)

hits = [slope_check(j[0], j[1]) for j in slopes]
a = 1
for j in hits:
    a *= j
print(a)
