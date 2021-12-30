def solve(parsed, steps):
    return len([i for i in range(steps, len(parsed)) if parsed[i] > parsed[i - steps]])


def main():
    with open("../../../inputs/2021/1.txt", "r") as f:
        parsed = [int(i.rstrip()) for i in f.readlines()]
    print(1, solve(parsed, 1))
    print(2, solve(parsed, 3))


if __name__ == "__main__":
    main()
