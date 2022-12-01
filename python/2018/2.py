with open("2.txt") as f:
    puzzle = f.read().splitlines()


def p1():
    two = 0
    three = 0
    for box in puzzle:
        letters = set(box)
        twos = False
        threes = False
        for l in letters:
            if box.count(l) == 2:
                twos = True
            if box.count(l) == 3:
                threes = True
        if twos:
            two +=1
        if threes:
            three += 1
    print("p1: ", two*three)

def p2():
    puzsort = sorted(puzzle)
    line_len = len(puzsort[0])
    different = 0    
    for line_i in range(1, len(puzsort)):
        for char_i in range(line_len):
            if puzsort[line_i][char_i] != puzsort[line_i -1][char_i]:
                different +=1
        if different == 1:
            solution = ''
            for char_i in range(line_len):
                if puzsort[line_i][char_i] == puzsort[line_i -1][char_i]:
                    solution += puzsort[line_i][char_i]
            print("p2: ", solution)
            break
        different = 0
p1()
p2()
