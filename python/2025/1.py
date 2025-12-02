def p1(myinput: str):
    pos = 50
    count = 0
    for line in myinput.split("\n"):
        direction = -1 if line.startswith("L") else 1
        pos += direction * int(line[1:])
        pos = pos % 100
        if pos == 0:
            count += 1
    return count


def solver(myinput: str):
    return p1(myinput), p2(myinput)


def p2(myinput: str):
    pos = 50
    count = 0
    for line in myinput.split("\n"):
        direction = -1 if line.startswith("L") else 1
        for _ in range(int(line[1:])):
            pos += direction
            pos %= 100
            if pos == 0:
                count += 1
    return count
