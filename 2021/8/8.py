def read_file(filename):
    with open(filename, "r") as f:
        data = [i.rstrip().split(" | ") for i in f.readlines()]

    return [([j for j in i[0].split(" ")], i[1].split()) for i in data]


def p1(content):
    counter = 0
    for line in content:
        usp, fdov = line
        for segments in fdov:
            if len(segments) in (2, 3, 4, 7):
                counter += 1
    return counter


def p2(content):
    segment_map = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6}
    solution = {1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None}
    for line in content:
        working = True
        while working:
            usp, fdov = line
            # line solution found, continue
            if None not in solution:
                working = False


def main():
    # filename = "example_input.txt"
    filename = "input.txt"
    content = read_file(filename)
    print(1, p1(content))
    print(2, p2(content))


if __name__ == "__main__":
    main()
