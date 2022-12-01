with open("1.txt") as f:
    freq = f.read().splitlines()

def p1():
    count = 0
    freqs = []
    for i in freq:
        count += int(i)
        freqs.append(count)
    print("1: ", count)

# part2 
def p2():
    seen = set()
    count = 0
    max_i = len(freq) -1
    i = 0
    while True:
        count += int(freq[i])
        if count in seen:
            print("2: ", count)
            break
        seen.add(count)

        i +=1
        if i> max_i:
            i=0

p1()
p2()
# 522753 too high
