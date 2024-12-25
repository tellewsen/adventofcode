import copy


def p1(filesystem: list[int | None]):
    fs = copy.copy(filesystem)
    maxlen = len(fs)
    j = maxlen
    for i in range(maxlen):
        if j <= i:
            break
        if fs[i] is not None:
            continue
        for k in range(j - 1, i, -1):
            if fs[k] is not None:
                fs[i] = fs[k]
                fs[k] = None
                j = k
                break
    return sum(i * v for i, v in enumerate(fs) if v is not None)


def str2fs(text: str) -> list[int | None]:
    fid = 0
    is_file = True
    filesystem = []
    for char in text.strip():
        if is_file:
            filesystem.extend([fid] * int(char))
            fid += 1
        else:
            filesystem.extend([None] * int(char))
        is_file = not is_file
    return filesystem


def solver(text: str):
    filesystem = str2fs(text)
    return p1(filesystem), p2(filesystem)


def p2(filesystem: list[int | None]):
    fs = copy.copy(filesystem)

    return sum(i * v for i, v in enumerate(fs) if v is not None)
