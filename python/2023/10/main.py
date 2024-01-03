"""
p1: Start at S. Walk the entire loop recording the number of steps. The
solution is at the halfway point.
"""


from math import ceil
import numpy as np
import pytest


@pytest.fixture
def example_input():
    with open("./example_input") as f:
        return f.readlines()


@pytest.fixture
def example_input2():
    with open("./example_input2") as f:
        return f.readlines()


def test_main(example_input, example_input2):
    assert p1(example_input) == 8
    assert p2(example_input2) == 10


def get_boundary(txt) -> set[tuple[int, int]]:
    """
    0: up
    1: down
    2: left
    3: right
    """
    for y1, line in enumerate(txt):
        S = line.find("S")
        if S >= 0:
            x1 = S
            break
    # x1, y1 is the start and the target
    x, y = x1, y1
    max_x = len(txt[0]) - 1
    max_y = len(txt) - 1
    ## Select which way to move first
    if x > 0 and txt[y][x - 1] in {"L", "F", "-"}:
        move = 2
    elif x < max_x and txt[y][x + 1] in {"-", "J", "7"}:
        move = 3
    elif y > 0 and txt[y - 1][x] in {"|", "7", "F"}:
        move = 0
    elif y < max_y and txt[y + 1][x] in {"|", "L", 'J"'}:
        move = 1
    else:
        raise ValueError("No connection found")
    boundary = {(x, y)}
    while True:
        match move:
            case 0:
                y -= 1
            case 1:
                y += 1
            case 2:
                x -= 1
            case 3:
                x += 1

        """
        0: up
        1: down
        2: left
        3: right
        """
        boundary.add((x, y))
        match txt[y][x]:
            # Change direction if we should turn
            case "L":
                move = 3 if move == 1 else 0
            case "J":
                move = 2 if move == 1 else 0
            case "F":
                move = 3 if move == 0 else 1
            case "7":
                move = 2 if move == 0 else 1
        if x == x1 and y == y1:
            break
    return boundary


def p1(txt: list[str]) -> int:
    return ceil(len(get_boundary(txt)) / 2)


def p2(txt):
    boundary = get_boundary(txt)
    area = 0
    for y,row in enumerate(txt):
        wall_count = 0
        for x,char in enumerate(row):
            if (x,y) in boundary:
                
            
        
    return


if __name__ == "__main__":
    with open("./input") as f:
        txt = f.readlines()
    print("p1: ", p1(txt))
    print("p2: ", p2(txt))
