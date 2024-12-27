import copy

import numpy as np


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
    text = "2333133121414131402"
    filesystem = str2fs(text)
    return p1(filesystem), p2(filesystem)


def p2(filesystem: list[int | None]):
    fs = copy.copy(filesystem)
    with open("test.txt", "w") as f:
        f.write(str(fs))
    max_id = len(fs)
    # We're going backwards
    f_idx = max_id - 1
    # print(fs)
    g_idx = 0
    while f_idx >= 0:
        # Ignore empty space
        if fs[f_idx] is None:
            f_idx -= 1
            continue
        # figure out size of candidate
        file = fs[f_idx]
        f_size = 1
        while f_idx - f_size >= 0 and fs[f_idx - f_size] == file:
            f_size += 1
        g_size = 0
        # print(file, f_size)
        # print(f_size)
        # look for a
        while g_idx < f_idx:
            if fs[g_idx] is None:
                g_size += 1
            else:
                g_size = 0
            # found a gap the file fits in, move it
            if g_size == f_size:
                print(g_idx, g_size, f_idx, fs[f_idx - f_size + 1 : f_idx + 1])
                for i in range(g_size):
                    fs[g_idx + i] = fs[f_idx - f_size + i]
                    fs[f_idx - f_size + i] = None
                g_size = 0
                break
            g_idx += 1
        # print(fs)

        f_idx -= f_size
    with open("test2.txt", "w") as f:
        f.write(str(fs))
    return sum(i * v for i, v in enumerate(fs) if v is not None)


# 15525011769356 high
# 15516529291883 high
