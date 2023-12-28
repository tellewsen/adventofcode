def get_line_matches(line):
    _, numbers = line.split(":")
    winning, my_nums = numbers.split("|")
    win_set = {int(i.strip()) for i in winning.strip().split() if i}
    my_set = {int(i.strip()) for i in my_nums.strip().split() if i}
    matches = len(win_set & my_set)
    return matches


def part1(lines):
    points = 0
    for line in lines:
        matches = get_line_matches(line)
        if not matches:
            continue
        points += 2 ** (matches - 1)
    return points


def part2(lines):
    line_matches = [get_line_matches(line) for line in lines]
    cards = [[j, 1] for j in line_matches]
    for i, card in enumerate(cards):
        card_matches, copies = card
        for j in range(1, card_matches + 1):
            cards[i + j][1] += copies
    return sum(card[1] for card in cards)


if __name__ == "__main__":
    with open("input") as f:
        lines = f.read().splitlines()

    print("p1: ", part1(lines))
    print("p2: ", part2(lines))
