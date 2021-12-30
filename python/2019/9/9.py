from collections import defaultdict

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
            vals.append(self.prog[self.index] if mode == 1 else
                        self.prog[self.prog[self.index] + self.rel_pos] if mode == 2
                        else self.prog[self.prog[self.index]])
            locs.append(None if mode == 1 else
                        self.prog[self.index] + self.rel_pos if mode == 2 else
                        self.prog[self.index])
            self.index += 1
        return op % 100, vals, locs

    def __call__(self):
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


def main():
    # read input
    foo = [int(i) for i in open('input').read().strip().split(',')]
    program = defaultdict(int)
    for i in range(len(foo)):
        program[i] = foo[i]

    # Part 1:
    foo = IntCode(program, 1)
    output = []
    try:
        while True:
            output.append(next(foo()))
    except StopIteration:
        print('halted')
    print(output)

    # Part 2:
    foo = IntCode(program, 2)
    output = []
    try:
        while True:
            output.append(next(foo()))
    except StopIteration:
        print('halted')
    print(output)


if __name__ == '__main__':
    main()
