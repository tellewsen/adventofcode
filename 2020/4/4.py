import re

with open('input') as f:
    file = f.read().split('\n\n')

stuff = [line.replace('\n', ' ').rstrip(' ') for line in file]
stuff2 = [line.split(' ') for line in stuff]
stuff3 = []
for line in stuff2:
    tempdict = {}
    for bar in line:
        k, v = bar.split(':')
        tempdict[k] = v
    stuff3.append(tempdict)

# Part 1
mandatory = ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid')
valid = len(stuff)
for e in stuff3:
    for i in mandatory:
        if i not in e:
            valid -= 1
            break
print(valid)

# Part 2
valid = len(stuff)
for e in stuff3:
    for i in mandatory:
        if i not in e:
            valid -= 1
            break
        value = e[i]
        if i == 'byr':
            if not 1920 <= int(value) <= 2002:
                valid -= 1
                break
        elif i == 'iyr':
            if not 2010 <= int(value) <= 2020:
                valid -= 1
                break
        elif i == 'eyr':
            if not 2020 <= int(value) <= 2030:
                valid -= 1
                break
        elif i == 'hgt':
            if value[-2:] == 'cm':
                if not 150 <= int(value[:-2]) <= 193:
                    valid -= 1
                    break
            elif value[-2:] == 'in':
                if not 59 <= int(value[:-2]) <= 76:
                    valid -= 1
                    break
            else:
                valid -= 1
                break
        elif i == 'hcl':
            if not re.match('^#[0-9a-f]{6}$', value):
                valid -= 1
                break
        elif i == 'ecl':
            if value not in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'):
                valid -= 1
                break
        elif i == 'pid':
            if not re.match('^[0-9]{9}$', value):
                valid -= 1
                break
print(valid)
