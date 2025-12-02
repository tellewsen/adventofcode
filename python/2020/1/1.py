with open("input") as f:
    numbers = f.read().splitlines()
numbers = [int(i) for i in numbers]

# part 1
for i in range(len(numbers)):
    for j in range(i, len(numbers)):
        if numbers[i] + numbers[j] == 2020:
            print(numbers[i] * numbers[j])
# part 2
for i in range(len(numbers)):
    for j in range(i, len(numbers)):
        for k in range(j, len(numbers)):
            if numbers[i] + numbers[j] + numbers[k] == 2020:
                print(numbers[i] * numbers[j] * numbers[k])
