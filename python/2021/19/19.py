def read_file(fname):
    with open(fname) as f:
        image = {}
        for i, line in enumerate(f.readlines()):
            if i == 0:
                algo = line.rstrip()
                continue
            for j, data in enumerate(line.rstrip()):
                image[(i - 2, j)] = data
        return algo, image
