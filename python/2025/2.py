def solver(myinput):
    return p1(myinput), p2(myinput)


def p1(myinput: str):
    ranges = myinput.split(",")
    solution = 0
    for rang in ranges:
        start, end = rang.split("-")
        start = int(start)
        end = int(end)
        for i in range(start, end):
            istr = str(i)
            a = istr[: len(istr) // 2]
            b = istr[len(istr) // 2 :]
            if a == b:
                solution += i
    return solution


def p2(myinput: str):
    ranges = myinput.split(",")
    solution = 0
    for rang in ranges:
        start, end = rang.split("-")
        start = int(start)
        end = int(end)
        for i in range(start, end):
            if haspattern(i):
                solution += i
    return solution


def haspattern(i: int) -> bool:
    istr = str(i)
    strlen = len(istr)
    for j in range(1, strlen):
        parts = strlen // j
        if istr[:j] * parts == istr:
            return True
    return False
