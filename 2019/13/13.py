import collections

import matplotlib.pyplot as plt
import numpy as np

num_locations = {1: 3,
                 2: 3,
                 3: 1,
                 4: 1,
                 5: 2,
                 6: 2,
                 7: 3,
                 8: 3,
                 9: 1,
                 99: 0}


class IntCode(object):

    def __init__(self, program, input_value=None):
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
            vals.append(self.prog[self.index] if mode == 1 else
                        self.prog[self.prog[self.index] + self.rel_pos] if mode == 2 else
                        self.prog[self.prog[self.index]])
            locs.append(None if mode == 1 else
                        self.prog[self.index] + self.rel_pos if mode == 2 else
                        self.prog[self.index])
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
                    "Weird value at pos {}: {} ".format(self.index, self.prog[self.index]))

            if self.index < 0:
                raise ValueError("Index negative")


def read_input():
    foo = [int(i) for i in open('input').read().strip().split(',')]
    program = collections.defaultdict(int)
    for i in range(len(foo)):
        program[i] = foo[i]
    return program


class ArcadeMachine(object):
    def __init__(self, program):
        self.screen = np.zeros((38, 21), dtype=int)
        self.output = []
        self.intcode = IntCode(program)

    def __call__(self, input_value=None):
        try:
            while True:
                if input_value is not None:
                    self.output.append(next(self.intcode(input_value)))
                else:
                    self.output.append(next(self.intcode()))
        except StopIteration:
            print('halted')

        for i in range(0, len(self.output), 3):
            self.screen[self.output[i]][self.output[i + 1]] = self.output[i + 2]

        return self.screen


def main():
    # read input
    program = read_input()

    # Part 1:
    game = ArcadeMachine(program.copy())
    screen = game()

    unique, counts = np.unique(screen, return_counts=True)
    print('Blocks on screen:', dict(zip(unique, counts))[2])

    # Part 2
    # Play for free
    game = ArcadeMachine(program.copy())
    game.intcode.prog[0] = 2
    output = []
    try:
        plt.imshow(np.rot90(screen, k=-1))
        plt.show()
        # move towards the ball
        screen = game()
        plt.imshow(np.rot90(screen, k=-1))
        plt.show()
    except StopIteration:
        print('halted')
    # for i in range(0, len(output), 3):
    #     screen[output[i]][output[i + 1]] = output[i + 2]




if __name__ == '__main__':
    main()
