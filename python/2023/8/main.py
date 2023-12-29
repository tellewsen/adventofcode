import math
import pytest


@pytest.fixture
def example_input():
    with open("./example_input") as f:
        lines = f.readlines()
    return lines


@pytest.fixture
def example_input2():
    with open("./example_input2") as f:
        lines = f.readlines()
    return lines


@pytest.fixture
def example_input3():
    with open("./example_input3") as f:
        lines = f.readlines()
    return lines


def test_parts(example_input, example_input2, example_input3):
    assert part1(*parse_lines(example_input)) == 2
    assert part1(*parse_lines(example_input2)) == 6
    assert part2(*parse_lines(example_input3)) == 6


def parse_lines(lines):
    instructions = lines[0].strip()
    nodes = {l[:3]: (l[7:10], l[12:15]) for l in lines[2:]}
    return instructions, nodes


def part1(instructions, nodes):
    current_node = "AAA"
    step_count = 0
    ins_idx = 0
    ins_idx_max = len(instructions) - 1
    while current_node != "ZZZ":
        # read instruction
        if ins_idx > ins_idx_max:
            ins_idx = 0
        side = instructions[ins_idx]
        ins_idx += 1
        # Move to next node
        next_node = nodes[current_node][0 if side == "L" else 1]
        current_node = next_node
        step_count += 1
    return step_count


def part2(instructions, nodes: dict[str, tuple[str, str]]):
    walkers = [k for k in nodes if k[2] == "A"]
    ins_idx = 0
    ins_idx_max = len(instructions) - 1
    step_count = 0
    needed_steps = []
    while walkers:
        step_count += 1
        if ins_idx > ins_idx_max:
            ins_idx = 0
        # Move to next node
        for index, w in enumerate(walkers):
            walkers[index] = nodes[w][0 if instructions[ins_idx] == "L" else 1]
        ins_idx += 1
        for w in walkers:
            if w[2] == "Z":
                needed_steps.append(step_count)
                walkers.remove(w)
    return math.lcm(*needed_steps)


if __name__ == "__main__":
    with open("./input") as f:
        lines = f.readlines()
    ins, nod = parse_lines(lines)
    print("p1: ", part1(ins, nod))
    print("p2: ", part2(ins, nod))
