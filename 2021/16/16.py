import sys


def read_file(filename):
    with open(filename, "r") as f:
        lines = f.readlines()[0].rstrip()
    return lines


def parse_packet(data, cursor, values):
    new_cursor = cursor
    value = ""
    version = int(data[cursor : cursor + 3], 2)
    type_id = int(data[cursor + 3 : cursor + 6], 2)
    cursor += 6
    if type_id == 4:  # literal value
        keep_going = True
        while keep_going:
            if data[cursor] == "0":  # last packet read and stop going
                keep_going = False
            value += data[cursor + 1 : cursor + 5]  # get the value
            cursor += 5
        cursor += 3
        print("value", value, int(value, 2))
        values.append(int(value, 2))
        # sys.exit()
    else:  # operator
        if data[cursor] == "0":
            cursor += 1
            # next 15 bits represent total length in bits
            length = int(data[cursor : cursor + 15], 2)
            print("length", length)
            cursor += 15
            value, cursor = parse_packet(data, cursor, values)
            print("value", value, int(value, 2))

        else:
            # next 11 bits represent number of sub-packets contained
            num_subpackets = int(data[cursor : cursor + 11], 2)
            print("num pack", num_subpackets)
            cursor += 11
            # value, cursor = parse_literal(data, cursor)
            # print("value2", value)

    return value, new_cursor, version


def p1(data):
    print(data)
    versions = []
    values = []
    cursor = 0
    while cursor < len(data):
        value, cursor, version = parse_packet(data, cursor, values)


def hex2bin(value):
    # prepend a 1 and remove it after to preserve leading zeros
    bin = "{0:b}".format(int("1" + value, 16))[1:]
    return bin


def main():
    # data = read_file("input.txt")
    data = read_file("ex.txt")
    p1(hex2bin(data))


if __name__ == "__main__":
    main()
