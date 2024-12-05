def solver(myinput: str):
    a = []
    a2 = {}
    b = []
    for line in myinput.splitlines():
        c, d = line.split("   ")
        a.append(int(c))
        a2[int(c)] = 0
        b.append(int(d))

    a = sorted(a)
    b = sorted(b)
    p1 = sum(abs(i[0] - i[1]) for i in zip(a, b))
    for k in b:
        if k in a2:
            a2[k] += 1
    return p1, sum(k * v for k, v in a2.items())
