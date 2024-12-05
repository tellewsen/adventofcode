def is_safe(result: list[int]) -> bool:
    increasing = result[1] > result[0]
    for i in range(len(result) - 1):
        if increasing and result[i + 1] < result[i]:
            return False
        if not increasing and result[i + 1] > result[i]:
            return False
        if not (0 < abs(result[i + 1] - result[i]) < 4):
            return False
    return True


def solver(myinput: str) -> tuple[int, int]:
    lines = [[int(i) for i in j.split()] for j in myinput.splitlines()]
    part1 = sum(is_safe(i) for i in lines)
    part2 = 0
    for line in lines:
        copies = [line[:i] + line[i + 1 :] for i in range(len(line))]
        for c in copies:
            if is_safe(c):
                part2 += 1
                break
    return part1, part2
