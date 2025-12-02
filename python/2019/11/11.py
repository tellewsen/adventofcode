import collections

import matplotlib.pyplot as plt
import numpy as np

num_locations = {1: 3, 2: 3, 3: 1, 4: 1, 5: 2, 6: 2, 7: 3, 8: 3, 9: 1, 99: 0}


class IntCode(object):
    def __init__(self, program, input_value):
        self.prog = program
        self.index = 0
        self.rel_pos = 0
        self.input_value = input_value

    def get_values(self):
        op = self.prog[self.index]
        self.index += 1
        vals = []
        locs = []
        for i in range(num_locations[op % 100]):
            mode = (op // (10 ** (2 + i))) % 10
            vals.append(
                self.prog[self.index]
                if mode == 1
                else self.prog[self.prog[self.index] + self.rel_pos]
                if mode == 2
                else self.prog[self.prog[self.index]]
            )
            locs.append(
                None
                if mode == 1
                else self.prog[self.index] + self.rel_pos
                if mode == 2
                else self.prog[self.index]
            )
            self.index += 1
        return op % 100, vals, locs

    def __call__(self, input_value=None):
        if input_value is not None:
            self.input_value = input_value
        while self.index < len(self.prog):
            opcode, vals, locs = self.get_values()

            if opcode == 99:
                raise StopIteration

            # Parse opcode and do the appropriate action
            if opcode == 1:
                self.prog[locs[2]] = vals[0] + vals[1]

            elif opcode == 2:
                self.prog[locs[2]] = vals[0] * vals[1]

            elif opcode == 3:
                self.prog[locs[0]] = self.input_value

            elif opcode == 4:
                yield vals[0]

            elif opcode == 5:
                if vals[0] != 0:
                    self.index = vals[1]

            elif opcode == 6:
                if vals[0] == 0:
                    self.index = vals[1]

            elif opcode == 7:
                self.prog[locs[2]] = 1 if vals[0] < vals[1] else 0

            elif str(opcode)[-1] == "8":
                self.prog[locs[2]] = 1 if vals[0] == vals[1] else 0

            elif str(opcode)[-1] == "9":
                self.rel_pos += vals[0]
            else:
                raise Exception(
                    "Weird value at pos {}: {} ".format(
                        self.index, self.prog[self.index]
                    )
                )

            if self.index < 0:
                raise ValueError("Index negative")


def robot(program, grid, start):
    directions = collections.OrderedDict(
        (
            ("U", [(0, 1), ("L", "R")]),
            ("R", [(1, 0), ("U", "D")]),
            ("D", [(0, -1), ("R", "L")]),
            ("L", [(-1, 0), ("D", "U")]),
        )
    )

    camera = IntCode(program, grid[start[0]][start[1]])
    pos = start
    direction = "U"
    painted_panels = set()
    try:
        while True:
            # Check output at position
            cur_color = grid[pos[0]][pos[1]]
            color = next(camera(cur_color))
            next_direction = next(camera())

            # Paint if not the right color
            if color != cur_color:
                grid[pos[0]][pos[1]] = color
                painted_panels.add(pos)  # keep track of which panels were painted

            # Switch direction
            direction = directions[direction][1][next_direction]

            # Move one step in that direction
            new_x = pos[0] + directions[direction][0][0]
            new_y = pos[1] + directions[direction][0][1]
            pos = (new_x, new_y)
    except StopIteration:
        print("halted")
    return grid, len(painted_panels)


def main():
    # read input
    foo = [int(i) for i in open("input").read().strip().split(",")]
    program = collections.defaultdict(int)
    for i in range(len(foo)):
        program[i] = foo[i]

    # Part 1:
    grid = np.zeros((1000, 1000), dtype=int)
    start = (200, 200)
    grid[start[0], start[1]] = 0
    _, painted_panels = robot(program, grid, start)

    # Part 2:
    grid = np.zeros((1000, 1000), dtype=int)
    start = (200, 200)
    grid[start[0], start[1]] = 1
    registration, _ = robot(program, grid, start)

    plt.imshow(registration)
    plt.show()


if __name__ == "__main__":
    main()
