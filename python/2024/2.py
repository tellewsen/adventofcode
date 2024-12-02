with open("input") as f:
    lines = [[int(i) for i in j.split()] for j in f.read().splitlines()]

def is_safe(result):
    increasing = result[1] > result[0]
    for i in range(len(result) - 1):
        if (
            increasing and result[i + 1] < result[i]):
            return False
        if not increasing and result[i + 1] > result[i]:
            return False
        if not (0 < abs(result[i + 1] - result[i]) < 4):
            return False
    return True

part1 = sum(is_safe(i) for i in lines)
print(part1)

safe = 0
for line in lines:
    copies = [line[:i]+line[i+1:] for i in range(len(line))]
    for c in copies:
        if is_safe(c):
            safe+=1
            break
print(safe)