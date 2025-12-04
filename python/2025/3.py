def solver(myinput):
    return solve(myinput, digit_n=2), solve(myinput)


def solve(myinput: str, digit_n: int = 12):
    tot = 0
    for line in myinput.split("\n"):
        best_digits = []
        jolts = list(map(int, line))
        last_index = -1
        for i in range(digit_n):
            candidates = jolts[last_index + 1 : len(jolts) - digit_n + 1 + i]
            best = max(candidates)
            last_index = candidates.index(best) + last_index + 1
            best_digits.append(best)
        a = "".join(map(str, best_digits))
        best = int(a)
        tot += best
    return tot
