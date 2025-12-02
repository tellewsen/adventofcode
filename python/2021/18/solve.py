def read_file(fname):
    with open(fname) as f:
        lines = []
        for line in f.readlines():
            lines.append(eval(line.rstrip()))
        return lines


def magnitude(line): ...


def reduce(line):
    while explode(line) or split(line):
        pass


def solve(lines):
    while len(lines) > 1:
        result = [lines[0], lines[1]]
        result = reduce(result)
        lines.pop(1)
        lines[0] = result
    print(magnitude(lines[0]))


solve(read_file("ex.txt"))
# solve(read_file('input.txt'))
