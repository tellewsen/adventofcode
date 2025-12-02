def read_file(filename):
    with open(filename, "r") as f:
        data = f.readlines()[0].rstrip().split(",")
    return [int(i) for i in data]


def get_ans(content, cost):
    minimum = min(content)
    maximum = max(content)
    answer = None
    for i in range(minimum, maximum + 1):
        ans = sum(cost(abs(j - i)) for j in content)
        if answer is None or ans < answer:
            answer = ans
    return answer


def p1(content):
    return get_ans(content, lambda x: x)


def p2(content):
    return get_ans(content, lambda x: x * (x + 1) / 2)


def main():
    content = read_file("input.txt")
    print(1, p1(content))
    print(2, p2(content))


if __name__ == "__main__":
    main()
