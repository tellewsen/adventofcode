def read_file(fname):
    with open(fname) as f:
        lines = [line.rstrip() for line in f.readlines()]
    return lines


def solve():
    # data = read_file("ex.txt")
    data = read_file("input.txt")
    on_set = set()
    for i, line in enumerate(data):
        print("processing line ", i)
        on_off, coords = line.split(" ")
        (
            x,
            y,
            z,
        ) = [i[2:] for i in coords.split(",")]
        xstart, xend = x.split("..")
        ystart, yend = y.split("..")
        zstart, zend = z.split("..")
        for x in range(int(xstart), int(xend) + 1):
            for y in range(int(ystart), int(yend) + 1):
                for z in range(int(zstart), int(zend) + 1):
                    if abs(z) > 50 or abs(y) > 50 or abs(x) > 50:
                        continue
                    if on_off == "on":
                        on_set.add((x, y, z))
                    else:
                        try:
                            on_set.remove((x, y, z))
                        except KeyError:
                            pass
    return len(on_set)


def main():
    print(1, solve())
    print(2, solve())


main()
