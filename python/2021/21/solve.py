import sys


def read_file(fname):
    with open(fname) as f:
        doc = f.readlines()
        p1 = int(doc[0].rstrip()[-1])
        p2 = int(doc[1].rstrip()[-1])
    return p1, p2


def roll_thrice(die):
    total = 0
    for _ in range(3):
        die += 1
        if die > 100:
            die -= 100
        total += die
    return die, total


def check_won(pscore):
    if pscore >= 1000:
        return True
    return False


def go_thrice(ploc, pscore, die, rolls, p2score):
    die, total = roll_thrice(die)
    rolls += 3
    ploc = (ploc + total) % 10
    ploc = 10 if ploc == 0 else ploc
    pscore += ploc
    if check_won(pscore):
        print(1, p2score*rolls)
        sys.exit(0)
    return ploc, pscore, die, rolls, p2score


def main():
    # p1loc, p2loc = read_file('input.txt')
    p1loc, p2loc = 4, 8
    p1score = 0
    p2score = 0
    rolls = 0
    die = 0

    while True:
        p1loc, p1score, die, rolls, p2score = go_thrice(
            p1loc, p1score, die, rolls, p2score)

        p2loc, p2score, die, rolls, p1score = go_thrice(
            p2loc, p2score, die, rolls, p1score)


print(main())

# low 160083 249696
# wrong 1624758 1244808 1295502 1161270 326196
