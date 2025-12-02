def read_file(filename):
    with open(filename, "r") as f:
        for i in f.readlines():
            return i.split(",")


def simulate(fish, n_days):
    fish_numbers = [0] * 9
    for i in fish:
        fish_numbers[i] += 1

    for i in range(n_days):
        temp_fish = fish_numbers[0]
        fish_numbers[0] = 0
        for i in range(8):
            fish_numbers[i] = fish_numbers[i + 1]
        fish_numbers[8] = temp_fish
        fish_numbers[6] += temp_fish

    return sum(fish_numbers)


def parse_fish(content):
    fish = []
    for i in content:
        fish.append(int(i))
    return fish


def main():
    content = read_file("input.txt")
    fishes = parse_fish(content)
    print(1, simulate(fishes, 80))
    print(2, simulate(fishes, 256))


if __name__ == "__main__":
    main()
