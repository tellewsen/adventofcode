with open("input") as f:
    file = [int(i) for i in f.read().splitlines()]

file.append(0)  # outlet
file.append(max(file) + 3)  # adapter
file = sorted(file)

one_jolt = 0
two_jolt = 0  # sanity check
three_jolt = 0

for i in range(len(file) - 1):
    diff = file[i + 1] - file[i]
    if diff == 1:
        one_jolt += 1
    elif diff == 2:
        two_jolt += 1
    elif diff == 3:
        three_jolt += 1
    else:
        print("error")

print("p1: ", one_jolt * three_jolt)

# Part 2
pc = {0: 1}
for a in file[1:]:
    pc[a] = pc.get(a - 3, 0) + pc.get(a - 2, 0) + pc.get(a - 1, 0)

print("p2: ", pc[file[-2]])
