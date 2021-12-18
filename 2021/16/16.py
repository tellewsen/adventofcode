import sys


def read_file(filename):
    with open(filename, "r") as f:
        lines = f.readlines()[0].rstrip()
    return lines


def parse_packet(data, old_cursor, values, versions):
    while old_cursor < len(data):
        new_cursor = old_cursor
        value = ""
        version = int(data[new_cursor: new_cursor + 3], 2)
        print('cursor', new_cursor, 'version', version)
        versions.append(version)
        new_cursor += 3
        type_id = int(data[new_cursor: new_cursor+3], 2)
        print('cursor', new_cursor, 'type', type_id)
        new_cursor += 3
        if type_id == 4:  # literal value
            keep_going = True
            round = 0
            while keep_going:
                if data[new_cursor] == "0":  # last packet read and stop going
                    keep_going = False
                value += data[new_cursor + 1: new_cursor + 5]  # get the value
                new_cursor += 5
                round += 1
            print("cursor", new_cursor, "value", int(value, 2))
            values.append(int(value, 2))
        else:  # operator
            print("cursor", new_cursor, "length type", data[new_cursor])
            if data[new_cursor] == "0":

                new_cursor += 1
                # next 15 bits represent total length in bits
                length = int(data[new_cursor: new_cursor + 15], 2)
                new_cursor += 15
                print("cursor", new_cursor, "length", length)
                end = new_cursor + length
                print("cursor before sub packet", new_cursor)
                while new_cursor < end:
                    print('cursor', new_cursor)
                    value, return_cursor = parse_packet(
                        data, new_cursor, values, versions)
                    new_cursor = return_cursor
                    print("value", value, int(value, 2))

            else:
                # next 11 bits represent number of sub-packets contained
                new_cursor += 1
                num_subpackets = int(data[new_cursor: new_cursor + 11], 2)
                print('cursor', new_cursor, "num pack", num_subpackets)
                new_cursor += 11
                for _ in range(num_subpackets):
                    value, return_cursor = parse_packet(
                        data, new_cursor, values, versions)
                    new_cursor = return_cursor
        return value, new_cursor


def p1(data):
    print(data, len(data))
    versions = []
    values = []
    cursor = 0
    parse_packet(data, cursor, values, versions)
    print('versions', versions)
    print("vsum", sum(versions))
    print('values', values)


def hex2bin(value):
    # prepend a 1 and remove it after to preserve leading zeros
    bin = "{0:b}".format(int("1" + value, 16))[1:]
    return bin


def main():
    data = read_file("input.txt")
    #data = read_file("ex.txt")
    p1(hex2bin(data))


if __name__ == "__main__":
    main()
