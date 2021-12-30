with open('input') as f:
    file = f.read().splitlines()
file = [line.replace('F', '0').replace('B', '1').replace('R', '1').replace('L', '0') for line in file]

foo = [(int(bar[:7], 2), int(bar[7:], 2)) for bar in file]
seatids = [i[0] * 8 + i[1] for i in foo]

# Part 1
print(max(seatids))

# Part 2
for i in range(min(foo)[0], max(foo)[0] + 1):
    for j in range(0, 8):
        if (i, j) not in foo:
            print((i, j), i * 8 + j)
