with open("input") as f:
    a = f.read().splitlines()

a = [i.split(" ") for i in a]

SCORE = {"A": 1, "B": 2, "C": 3}
WIN = {
    "A": "C",  # rock -> sci
    "B": "A",  # pap > rock
    "C": "B",  # sci -> pap
}
RESPONSE = {"X": "A", "Y": "B", "Z": "C"}
LOSE = {
    "A": "B",
    "B": "C",
    "C": "A",
}


def choose(choice, want):
    if want == "X":
        return WIN[choice]
    if want == "Y":
        return choice
    if want == "Z":
        return LOSE[choice]
    else:
        raise ValueError


def p1():
    score = 0
    for o, p in a:
        score += SCORE[RESPONSE[p]]
        score += 6 if WIN[RESPONSE[p]] == o else 0
        score += 3 if RESPONSE[p] == o else 0
    print(score)


def p2():
    score = 0
    for o, p in a:
        choice = choose(o, p)
        score += SCORE[choice]
        score += 6 if p == "Z" else 0
        score += 3 if p == "Y" else 0
    print(score)


p1()
p2()
