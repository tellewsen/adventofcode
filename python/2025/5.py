def solver(myinput: str):
    return p1(myinput), p2(myinput)


def isfresh(id, ranges):
    for rang in ranges:
        if rang[0] <= int(id) <= rang[1]:
            return True
    return False


def p1(inp: str):
    frshcnt = 0
    fresh, available = inp.split("\n\n")
    frshrang = []
    for line in fresh.split("\n"):
        start, end = line.split("-")
        frshrang.append((int(start), int(end)))
    for line in available[:-1].split("\n"):
        if isfresh(line, frshrang):
            frshcnt += 1

    return frshcnt


def merge_ranges(ranges):
    """Merge overlapping ranges efficiently."""

    sorted_ranges = sorted(ranges)
    merged = [sorted_ranges[0]]

    for current_start, current_end in sorted_ranges[1:]:
        last_start, last_end = merged[-1]

        if current_start <= last_end + 1:
            merged[-1] = (last_start, max(last_end, current_end))
        else:
            merged.append((current_start, current_end))
    return merged


def p2(inp):
    fresh, _ = inp.split("\n\n")
    frshrang = []
    for line in fresh.split("\n"):
        start, end = line.split("-")
        frshrang.append((int(start), int(end)))

    # Merge overlapping ranges
    merged = merge_ranges(frshrang)

    # Count total values in merged ranges
    total = sum(end - start + 1 for start, end in merged)
    return total


# 440412941379409 high
