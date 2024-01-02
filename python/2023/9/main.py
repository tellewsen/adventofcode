# TODO: This screams pascals triangle shenanigans. Figure out if
# there's something smart that can be done with that
import pytest


def read_lines(fname: str):
    with open(fname) as f:
        return [[int(i) for i in l.split()] for l in f.readlines()]


@pytest.fixture
def example_lines():
    return read_lines("./example_input")


def test_p1(example_lines):
    assert p1(example_lines) == 114
    assert p2(example_lines) == 2


def solve(line: list[int], p2=False):
    # down
    rows = [line]
    while any(rows[-1]):
        next_line = [rows[-1][i + 1] - rows[-1][i] for i in range(0, len(rows[-1]) - 1)]
        rows.append(next_line)
    # up
    new_end = 0
    for i in range(len(rows) - 1, 0, -1):
        cur_end = rows[i - 1][0 if p2 else -1]
        new_end = cur_end - new_end if p2 else cur_end + new_end
    return new_end


def p2(lines: list[list[int]]):
    return sum(solve(line, True) for line in lines)


def p1(lines: list[list[int]]):
    next_vals = []
    for line in lines:
        next_vals.append(solve(line))
    return sum(next_vals)


if __name__ == "__main__":
    rows = read_lines("./input")
    print("p1: ", p1(rows))
    print("p2: ", p2(rows))
