INPUT_VALUE = 5


# Part 1
def intcode(ins, input_value):
    index = 0
    while index < len(ins):
        opcode = ins[index]
        mode = [0, 0, 0]
        if opcode == 99:
            return 'FINISHED'

        # Set the parameter mode
        value = str(ins[index])
        if len(value) == 5:
            mode[0] = int(value[2])
            mode[1] = int(value[1])
            mode[2] = int(value[0])
        elif len(value) == 4:
            mode[0] = int(value[1])
            mode[1] = int(value[0])
        elif len(value) == 3:
            mode[0] = int(value[0])

        a = ins[index + 1] if mode[0] else ins[ins[index + 1]]
        try:
            b = ins[index + 2] if mode[1] else ins[ins[index + 2]]
        except Exception:
            pass
        if str(opcode)[-1] == "1":
            ins[ins[index + 3]] = a + b
            index += 4
        elif str(opcode)[-1] == "2":
            ins[ins[index + 3]] = a * b
            index += 4
        elif str(opcode)[-1] == "3":
            ins[ins[index + 1]] = input_value
            index += 2
        elif str(opcode)[-1] == "4":
            print('OUTPUT: ', a)
            if a != 0:
                break
            index += 2
        elif str(opcode)[-1] == "5":
            index = b if a != 0 else index + 3
        elif str(opcode)[-1] == "6":
            index = b if a == 0 else index + 3
        elif str(opcode)[-1] == "7":
            ins[ins[index + 3]] = 1 if a < b else 0
            index += 4
        elif str(opcode)[-1] == "8":
            ins[ins[index + 3]] = 1 if a == b else 0
            index += 4
        else:
            raise Exception(
                "Weird value at pos {}: {} ".format(index, ins[index]))


with open('input', 'r') as f:
    data = f.read()
    instructions = [int(i) for i in data.split(',')]

    print("Part #1:")
    input_value = 1
    intcode(instructions.copy(), input_value)

    print("Part #2:")
    input_value = 5
    intcode(instructions.copy(), input_value)
