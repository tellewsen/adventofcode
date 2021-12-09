def p1(a):
    print(a)
    return


def p2():
    return


with open("input.txt", "r") as f:
    data = [i.rstrip() for i in f.readlines()]

for line in data:
    start, stop = line.split(" -> ")
    x1, y1 = start.split(",")
    x2, y2 = stop.split(",")
    x1 = int(x1)
    x2 = int(x2)
    y1 = int(y1)
    y2 = int(y2)
    gradient = (y2 - y1) / (x2 - x1)

print(1, p1(data))
print(2, p2())
