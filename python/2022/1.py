with open("input") as f:
    cals = f.read().splitlines()

elves = []
sums = 0
for i in cals:
    if i == '':
        elves.append(sums)
        sums = 0
        continue
    sums += int(i)

print(max(elves)) # 1 
print(sum(sorted(elves)[-3:])) # 2
