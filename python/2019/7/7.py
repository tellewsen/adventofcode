import itertools


class Amplifier(object):
    def __init__(self, program, phase):
        self.prog = program
        self.phase = phase
        self.index = 0
        self.phase_read = False

    def __call__(self, input_value):
        self.input_value = input_value

        def parse_mode(mode_op):
            mode_a = (mode_op // 100) % 10
            mode_b = (mode_op // 1000) % 10
            mode_c = (mode_op // 10000) % 10
            return mode_a, mode_b, mode_c

        while self.index < len(self.prog):
            opcode = self.prog[self.index]
            if opcode == 99:
                raise StopIteration

            # Set the parameter mode
            mode = parse_mode(opcode)

            a = (
                self.prog[self.index + 1]
                if mode[0]
                else self.prog[self.prog[self.index + 1]]
            )
            try:
                b = (
                    self.prog[self.index + 2]
                    if mode[1]
                    else self.prog[self.prog[self.index + 2]]
                )
            except Exception:
                pass
            if str(opcode)[-1] == "1":
                self.prog[self.prog[self.index + 3]] = a + b
                self.index += 4
            elif str(opcode)[-1] == "2":
                self.prog[self.prog[self.index + 3]] = a * b
                self.index += 4
            elif str(opcode)[-1] == "3":
                if self.phase_read:
                    self.prog[self.prog[self.index + 1]] = self.input_value
                else:
                    self.prog[self.prog[self.index + 1]] = self.phase
                    self.phase_read = True
                self.index += 2
            elif str(opcode)[-1] == "4":
                self.index += 2
                return a
            elif str(opcode)[-1] == "5":
                self.index = b if a != 0 else self.index + 3
            elif str(opcode)[-1] == "6":
                self.index = b if a == 0 else self.index + 3
            elif str(opcode)[-1] == "7":
                self.prog[self.prog[self.index + 3]] = 1 if a < b else 0
                self.index += 4
            elif str(opcode)[-1] == "8":
                self.prog[self.prog[self.index + 3]] = 1 if a == b else 0
                self.index += 4
            else:
                raise Exception(
                    "Weird value at pos {}: {} ".format(
                        self.index, self.prog[self.index]
                    )
                )

            # if self.index > len(self.prog):
            #     self.index -= len(self.prog)


def main():
    amplifier_program = [int(i) for i in open("input").read().strip().split(",")]

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

    phases = list(itertools.permutations([5, 6, 7, 8, 9]))
    best = [0, 0]
    for phase in phases:
        amplifiers = []
        for i in range(len(phase)):
            amplifiers.append(Amplifier(amplifier_program.copy(), phase[i]))
        signal = 0
        halt = False
        while not halt:
            try:
                for j, amplifier in enumerate(amplifiers):
                    signal = amplifier(signal)
            except StopIteration:
                halt = True
        result = [phase, signal]
        if result[1] > best[1]:
            best = result
    print("Part #2:", best)


if __name__ == "__main__":
    main()
