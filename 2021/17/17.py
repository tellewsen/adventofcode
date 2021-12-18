def read_file(filename):
    with open(filename, "r") as f:
        lines = f.readlines()[0].rstrip()
    x, y = lines.split(': ')[1].split(', ')
    xstart, xstop = x.split('=')[1].split('..')
    x = [i for i in range(int(xstart), int(xstop)+1)]
    ystart, ystop = y.split('=')[1].split('..')
    y = [i for i in range(int(ystart), int(ystop)+1)]
    return x, y


def go_one_step(x, y, vx, vy):
    x += vx
    y += vy
    if vx > 0:
        vx -= 1
    elif vx < 0:
        vx += 1
    vy -= 1
    return x, y, vx, vy


def launch(vx, vy, x_target, y_target):
    x = 0
    y = 0
    max_y = 0
    while y >= min(y_target) and x <= max(x_target) and not (vx == 0 and x not in x_target):
        x, y, vx, vy = go_one_step(x, y, vx, vy)
        if y > max_y:  # keep track of max height
            max_y = y
        if x in x_target and y in y_target:
            return True, max_y
    return False, max_y


def solve(data):
    x_target, y_target = data
    winner_y = 0
    won = 0
    for vx in range(1, max(x_target)*2):
        for vy in range(min(y_target), max(x_target)):
            hit, max_y = launch(vx, vy, x_target, y_target)
            if hit:
                won += 1
                if max_y > winner_y:
                    winner_y = max_y

    print(1, winner_y)
    print(2, won)


solve(read_file("input.txt"))
