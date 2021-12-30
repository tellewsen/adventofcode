d = {'E': 1, 'S': -1j, 'W': -1, 'N': 1j}
with open('input') as f:
    inst = [(i[0], int(i[1:])) for i in f.read().splitlines()]


def solve(part):
    pos = 0 + 0j
    way = 1 + 0j if part == 1 else 10 + 1j
    for i, step in inst:
        if i == 'F':
            pos += step * way
        elif i == 'L':
            way *= 1j ** (step/90)
        elif i == 'R':
            way *= 1j ** (-step/90)
        elif part == 1:
            pos += step*d[i]
        elif part == 2:
            way += step*d[i]
    return int(abs(pos.real) + abs(pos.imag))


print('p1: ', solve(1))
print('p2: ', solve(2))

