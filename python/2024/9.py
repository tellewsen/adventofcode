def solver(text):
    fid = 0
    is_file = True
    filesystem = []
    for char in text.strip():
        if is_file:
            for _ in range(int(char)):
                filesystem.append(fid)
            fid += 1
        else:
            for _ in range(int(char)):
                filesystem.append(None)
        is_file = not is_file
    with open("test1.txt", "w") as f:
        f.write(",".join((str(i) for i in filesystem)))

    maxlen = len(filesystem)
    j = maxlen
    for i in range(maxlen):
        if j <= i:
            break
        if filesystem[i] is not None:
            continue
        for k in range(j - 1, i, -1):
            if filesystem[k] is not None:
                filesystem[i] = filesystem[k]
                filesystem[k] = None
                j = k
                break
    with open("test2.txt", "w") as f:
        f.write(",".join((str(i) for i in filesystem)))
    return sum(i * v for i, v in enumerate(filesystem) if v is not None), 1
