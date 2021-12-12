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


def solve(line):
    solution = {1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None}
    usp, fdov = line
    # step 0
    for element in usp:
        # These are the only ones with their respective lengths
        if len(element) == 2:
            solution[1] = "".join(sorted(element))
        elif len(element) == 3:
            solution[7] = "".join(sorted(element))
        elif len(element) == 4:
            solution[4] = "".join(sorted(element))
        elif len(element) == 7:
            solution[8] = "".join(sorted(element))
    # step 1
    for element in usp:
        # Removing 7+4 leaves 1 line on 9
        if len(element) == 6:
            checkchars = solution[7] + solution[4]
            char_in_element = element
            for i in checkchars:
                char_in_element = char_in_element.replace(i, "")
            if len(char_in_element) == 1:
                solution[9] = "".join(sorted(element))
    # step 2
    for element in usp:
        if len(element) == 6 and "".join(sorted(element)) != solution[9]:
            # Removing 1 leaves 4 lines on 0
            # Remaining must be 6
            char_in_element = element
            for i in solution[1]:
                char_in_element = char_in_element.replace(i, "")
            if len(char_in_element) == 4:
                solution[0] = "".join(sorted(element))
            else:
                solution[6] = "".join(sorted(element))
    # step 3
    for element in usp:
        if len(element) == 5:
            # Removing 1 leaves 3 lines on 3
            # Removing 9 leaves 0 lines on 5
            check3 = element
            for i in solution[1]:
                check3 = check3.replace(i, "")
            check0 = element
            for i in solution[9]:
                check0 = check0.replace(i, "")
            if len(check3) == 3:
                solution[3] = "".join(sorted(element))
            elif len(check0) == 0:
                solution[5] = "".join(sorted(element))
            else:
                solution[2] = "".join(sorted(element))
    # line solution found, return it
    a = {"".join(sorted(k)): v for v, k in solution.items()}
    val = ""
    for e in fdov:
        val += str(a["".join(sorted(e))])
    return int(val)


def p2(content):
    answer = 0
    for line in content:
        answer += solve(line)
    return answer


def main():
    filename = "input.txt"
    content = read_file(filename)
    print(1, p1(content))
    print(2, p2(content))


if __name__ == "__main__":
    main()
