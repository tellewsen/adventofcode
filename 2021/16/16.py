def read_file(filename):
    with open(filename, "r") as f:
        lines = f.readlines()[0].rstrip()
    return lines


def parse_packet(data, cursor, versions):
    version = int(data[cursor: cursor + 3], 2)
    versions.append(version)
    type_id = int(data[cursor + 3: cursor + 6], 2)
    cursor += 6
    if type_id == 4:  # literal value
        value = ""
        keep_going = True
        while keep_going:
            if data[cursor] == "0":  # last packet read stop after
                keep_going = False
            value += data[cursor + 1: cursor + 5]  # get the value
            cursor += 5
        return int(value, 2), cursor
    sub_values = []
    if data[cursor] == "0":  # 15 bit length
        length = int(data[cursor+1: cursor + 16], 2)
        cursor += 16
        end = cursor + length
        while cursor < end:
            value, cursor = parse_packet(
                data, cursor, versions)
            sub_values.append(value)
    else:  # 11 bit length
        num_subpackets = int(data[cursor+1: cursor + 12], 2)
        cursor += 12
        for _ in range(num_subpackets):
            value, cursor = parse_packet(
                data, cursor, versions)
            sub_values.append(value)
    if type_id == 0:
        val = sum(sub_values)
    elif type_id == 1:
        if len(sub_values) == 1:
            val = sub_values[0]
        else:
            val = 1
            for v in sub_values:
                val *= v
    elif type_id == 2:
        val = min(sub_values)
    elif type_id == 3:
        val = max(sub_values)
    elif type_id == 5:
        val = 1 if sub_values[0] > sub_values[1] else 0
    elif type_id == 6:
        val = 1 if sub_values[0] < sub_values[1] else 0
    elif type_id == 7:
        val = 1 if sub_values[0] == sub_values[1] else 0
    return val, cursor


def solve(data):
    versions = []
    ans, _ = parse_packet(data, 0, versions)
    print(1, sum(versions))
    print(2, ans)


def hex2bin(value):
    # prepend a 1 and remove it after to preserve leading zeros
    bin = "{0:b}".format(int("1" + value, 16))[1:]
    return bin


def main():
    data = read_file("input.txt")
    solve(hex2bin(data))


if __name__ == "__main__":
    main()
