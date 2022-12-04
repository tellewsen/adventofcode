answer_1 = 0
answer_2 = 0
with open("input") as f:
    for line in f.readlines():
        line = line.rstrip("\n")
        a, b = line.split(",")
        a_0, a_1 = a.split("-")
        b_0, b_1 = b.split("-")
        a = set(i for i in range(int(a_0), int(a_1) + 1))
        b = set(i for i in range(int(b_0), int(b_1) + 1))
        c = a.intersection(b)
        if a == c or b == c:
            answer_1 += 1
        if len(c) > 0:
            answer_2 += 1
print(answer_1)
print(answer_2)
