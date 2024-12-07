def pag_is_okay(pag: list[int], rules):
    for rul in rules:
        if rul[0] in pag and rul[1] in pag:
            candidates = pag.index(rul[0]), pag.index(rul[1])
            if candidates[0] > candidates[1]:
                return candidates
    return None


def solver(text: str):
    rulestext, rest = text.split("\n\n")
    rules = []
    for i in rulestext.splitlines():
        a, b = i.split("|")
        rules.append((int(a), int(b)))
    pages = [[int(j) for j in i.split(",")] for i in rest.splitlines()]
    midpagesum = 0
    badpages = []
    for pag in pages:
        if pag_is_okay(pag, rules) is None:
            midpagesum += pag[len(pag) // 2]
        else:
            badpages.append(pag)

    badpaglen = len(badpages)
    for i in range(badpaglen):
        while candidates := pag_is_okay(badpages[i], rules):
            if candidates is None:
                continue
            j, k = candidates
            badpages[i][j], badpages[i][k] = badpages[i][k], badpages[i][j]
    return midpagesum, sum(pag[len(pag) // 2] for pag in badpages)
