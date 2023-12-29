with open("input.txt") as f:
    lines = f.read().splitlines()

numbers = []
replacements = {
    "one": "one1one",
    "two": "two2two",
    "three": "three3three",
    "four": "four4four",
    "five": "five5five",
    "six": "six6six",
    "nine": "nine9nine",
    "eight": "eight8eight",
    "seven": "seven7seven",
}
for line in lines:
    num = ""
    for k, v in replacements.items():
        line = line.replace(k, v)
    for char in line:
        if char.isdigit():
            num += char
    val = int(num[0] + num[-1])
    print(line, val)
    numbers.append(val)
print(sum(numbers))

# 49841 low
# 49900 low
# 54530
