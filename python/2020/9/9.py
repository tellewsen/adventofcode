with open('input') as f:
    file = f.read().splitlines()
file = [int(i) for i in file]

preamble_length = 25


def get_possible_sums(number_list):
    possible = set()
    for i in range(len(number_list)):
        for j in number_list[i:]:
            possible.add(number_list[i]+j)
    return possible


# Part 1
def part1():
    for i in range(25, len(file)):
        foo = file[i-25:i]
        possible = get_possible_sums(foo)
        if not file[i] in possible:
            return file[i]


# Part 2
def part2(target_number):
    length = 2
    while True:
        for i in range(len(file)):
            numbers = file[i:i+length]
            if sum(numbers) == target_number:
                print(numbers)
                return sum((min(numbers), max(numbers)))
        length += 1


def main():
    target_number = part1()
    print('part1: ', target_number)
    print('part2: ', part2(target_number))


if __name__ == '__main__':
    main()
