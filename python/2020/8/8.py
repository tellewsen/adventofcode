import copy
import typing


def read_input(filename):
    with open(filename) as f:
        return f.read().splitlines()


def acc(accumulator, instructions_now, value):
    accumulator += value
    instructions_now += 1
    return accumulator, instructions_now


def jmp(accumulator, instructions_now, value):
    instructions_now += value
    return accumulator, instructions_now


def nop(accumulator, instructions_now, value):
    instructions_now += 1
    return accumulator, instructions_now


actions = {
    "acc": acc,
    "jmp": jmp,
    "nop": nop,
}


def prep_instructions(file) -> typing.List[typing.List[typing.Union[str, int]]]:
    instructions = []
    for i in range(len(file)):
        foo = file[i].split(" ")
        instructions.append([foo[0], int(foo[1])])
    return instructions


def part1(instructions):
    len_inst = len(instructions)
    accumulator = 0
    no_repeats = True
    instructions_done = []
    instructions_now = 0
    while no_repeats:
        if instructions_now == len_inst:
            code = "ok"
            break
        if instructions_now in instructions_done:
            code = "inf"
            break
        instructions_done.append(instructions_now)
        instruction = instructions[instructions_now]
        accumulator, instructions_now = actions[instruction[0]](
            accumulator, instructions_now, instruction[1]
        )
    return code, accumulator


def part2(instructions):
    for i in range(len(instructions)):
        instructions_copy = copy.deepcopy(instructions)
        if instructions_copy[i][0] == "jmp":
            instructions_copy[i][0] = "nop"
        elif instructions_copy[i][0] == "nop":
            instructions_copy[i][0] = "jmp"
        else:
            continue
        code, accu = part1(instructions_copy)
        if code == "ok":
            break
    return code, accu


def main():
    file = read_input("input")
    instructions = prep_instructions(file)
    print("p1: ", part1(instructions))
    print("p2: ", part2(instructions))


if __name__ == "__main__":
    main()
