with open("input.txt", "r") as f:
    a = [i.rstrip() for i in f.readlines()]


def p1():
    epsilon = ""
    gamma = ""
    nlines = len(a)
    linelen = len(a[0])
    for j in range(linelen):
        count = 0
        for i in range(nlines):
            count += int(a[i][j])
        if count / nlines > 0.5:
            gamma += "1"
            epsilon += "0"
        if count / nlines < 0.5:
            epsilon += "1"
            gamma += "0"
    return int(gamma, 2) * int(epsilon, 2)


def p2():
    def counter(inputlines, index, co2count):
        if len(inputlines) == 1:
            return inputlines[0]
        keep = []
        numbers = []
        for line in inputlines:
            numbers += line[index]
        if numbers.count("1") >= numbers.count("0"):
            number = "0" if co2count else "1"
        else:
            number = "1" if co2count else "0"
        for line in inputlines:
            if line[index] == number:
                keep.append(line)
        return counter(keep, index + 1, co2count)

    ogr = counter(a, 0, False)
    csr = counter(a, 0, True)
    return int(ogr, 2) * int(csr, 2)


print(1, p1())
print(2, p2())
