import math

with open("input") as f:
    file = f.read().splitlines()


def solve1(lines):
    arr = int(lines[0])
    busses = [int(i) for i in lines[1].split(",") if i != "x"]
    temp = [math.ceil(arr / i) * i for i in busses]
    wait = min(temp)
    bid = busses[temp.index(wait)]
    return int((wait - arr) * bid)


p1test = """939
7,13,x,x,59,x,31,19
""".splitlines()
print("p1func is: ", "OK" if solve1(p1test) == 295 else "bad")
print("p1 :", solve1(file))

p2tests = [
    ("17,x,13,19", 3417),
    ("67,7,59,61", 754018),
    ("67,x,7,59,61", 779210),
    ("67,7,x,59,61", 1261476),
    ("1789,37,47,1889", 1202161486),
]


def solve2(line):
    busses = [(int(j), i) for i, j in enumerate(line.split(",")) if j.isdigit()]
    t = 0
    step = busses[0][0]
    for bus_id, offset in busses[1:]:
        while (t + offset) % bus_id != 0:
            t += step
        step *= bus_id
    return t


for k in p2tests:
    print("p2func is: ", "OK" if solve2(k[0]) == k[1] else "bad")
print("p2: ", solve2(file[1]))
