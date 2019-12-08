import itertools


class Amplifier(object):
    def __init__(self, program, phase):
        self.prog = program
        self.phase = phase
        self.input_values = []

    def __call__(self, input_value):
        self.input_value = input_value
        phase_read = False

        def parse_mode(mode_op):
            mode_a = (mode_op // 100) % 10
            mode_b = (mode_op // 1000) % 10
            mode_c = (mode_op // 10000) % 10
            return mode_a, mode_b, mode_c

        index = 0
        while index < len(self.prog):
            opcode = self.prog[index]
            if opcode == 99:
                raise StopIteration

            # Set the parameter mode
            mode = parse_mode(opcode)

            a = self.prog[index + 1] if mode[0] else self.prog[
                self.prog[index + 1]]
            try:
                b = self.prog[index + 2] if mode[1] else self.prog[
                    self.prog[index + 2]]
            except Exception:
                pass
            if str(opcode)[-1] == "1":
                self.prog[self.prog[index + 3]] = a + b
                index += 4
            elif str(opcode)[-1] == "2":
                self.prog[self.prog[index + 3]] = a * b
                index += 4
            elif str(opcode)[-1] == "3":
                if phase_read:
                    if mode[1]:
                        self.prog[index + 1] = self.input_value
                    else:
                        self.prog[self.prog[index + 1]] = self.input_value
                else:
                    if mode[1]:
                        self.prog[index + 1] = self.phase
                    else:
                        self.prog[self.prog[index + 1]] = self.phase
                    phase_read = True
                index += 2
            elif str(opcode)[-1] == "4":
                # print('returning', a)
                return a
            elif str(opcode)[-1] == "5":
                index = b if a != 0 else index + 3
            elif str(opcode)[-1] == "6":
                index = b if a == 0 else index + 3
            elif str(opcode)[-1] == "7":
                self.prog[self.prog[index + 3]] = 1 if a < b else 0
                index += 4
            elif str(opcode)[-1] == "8":
                self.prog[self.prog[index + 3]] = 1 if a == b else 0
                index += 4
            else:
                raise Exception(
                    "Weird value at pos {}: {} ".format(index,
                                                        self.prog[index]))


def main():
    amplifier_program = [int(i) for i in
                         open('input').read().strip().split(',')]

    phase = [0, 1, 2, 3, 4]
    phases = list(itertools.permutations(phase))
    best = [0, 0]

    for phase in phases:
        signal = 0
        for val in phase:
            input_value = signal
            signal = Amplifier(amplifier_program.copy(), val)(input_value)
        if signal > best[1]:
            best = [phase, signal]
    print("Part #1:", best)

    phase = [5, 6, 7, 8, 9]
    phases = list(itertools.permutations(phase))

    # test
    # should have max thruster signal 139629729
    amplifier_program = [3, 52, 1001, 52, -5, 52, 3, 53, 1, 52, 56, 54, 1007,
                         54, 5, 55, 1005, 55, 26, 1001, 54, -5, 54, 1105, 1,
                         12, 1, 53, 54, 53, 1008, 54, 0, 55, 1001, 55, 1, 55,
                         2, 53, 55, 53, 4, 53, 1001, 56, -1, 56, 1005, 56, 6,
                         99, 0, 0, 0, 0, 10]
    phases = [[9, 7, 8, 5, 6]]

    best = [0, 0]
    for phase in phases:
        foo = amplifier_program.copy()
        amplifiers = [Amplifier(foo, i) for i in phase]
        signal = 0
        halt = False
        a = 0

        while not halt:
            # print("round:", a)
            for amplifier in amplifiers:
                try:
                    # print('signal_before:',signal)
                    signal = amplifier(signal)
                    print('signal_after:', signal)
                except StopIteration:
                    halt = True
                    print("halting")
            a += 1
            result = [phase, signal]
            print(result)
            if result[1] > best[1]:
                best = result
    print("Part #2:", best)


if __name__ == '__main__':
    main()
