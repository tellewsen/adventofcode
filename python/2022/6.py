with open("input") as f:
    a = f.read()


def count(chars):
    for i in range(chars, len(a)):
        b = set(i for i in a[i - chars : i])
        if len(b) == chars:
            return i


print("1: ", count(4))
print("2: ", count(14))
