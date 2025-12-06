import functools
import re

import numpy as np


def solver(myinput: str):
    return p1(myinput), p2(myinput)


def p1(inp: str):
    grid = []
    for line in inp.split("\n"):
        numbers = re.findall(r"([^\s]+)", line)
        grid.append([num for num in numbers])
    ops = grid[-1]
    numbs = grid[:-1]
    total = 0
    for i in range(len(numbs[0])):
        op_f = ops[i]
        if op_f == "*":
            op = lambda x, y: x * int(y)
            identity = 1
        elif op_f == "+":
            op = lambda x, y: x + int(y)
            identity = 0
        else:
            raise ValueError("Unknown operation")
        sumcol = functools.reduce(
            lambda sumcol, x: op(sumcol, int(x[i])), numbs, identity
        )
        total += sumcol
    return total


def p2(myinput: str):
    grid = np.array([[i for i in line] for line in myinput.split("\n")])
    # rotate and flip
    transposed = grid.T[::-1]
    total = 0
    working_numbers = []
    for row in transposed:
        # collect numbers until we hit an operator
        numbers_on_row = row[:-1]
        digits = "".join([i for i in numbers_on_row if i.isdigit()])
        try:
            working_numbers.append(int(digits))
        except ValueError:
            # empty column
            continue
        op = row[-1]
        if op == "*":
            op_f = lambda x, y: x * int(y)
            identity = 1
        elif op == "+":
            op_f = lambda x, y: x + int(y)
            identity = 0
        else:
            # no operator, keep collecting
            continue
        # Found an operator, apply it to the collected numbers and reset list
        total += functools.reduce(lambda x, y: op_f(x, y), working_numbers, identity)
        working_numbers = []
    return total
