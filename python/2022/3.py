with open("input") as f:
    ruck = f.read().splitlines()


def p1():
    pris = 0
    for line in ruck:
        a = set(line[: len(line) // 2])
        b = set(line[len(line) // 2 :])
        p = list(a & b)
        v = ord(p[0])
        if v > 96:
            v = v - 96
        else:
            v = v - 38
        pris += v
    print(pris)


def p2():
    pris = 0
    for i in range(0, len(ruck), 3):
        p = list(set(ruck[i]) & set(ruck[i + 1]) & set(ruck[i + 2]))
        v = ord(p[0])
        if v > 96:
            v = v - 96
        else:
            v = v - 38
        pris += v
    print(pris)


p1()
p2()
